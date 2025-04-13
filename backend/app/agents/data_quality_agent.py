import os
import sys
import json
import pandas as pd

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))

from app.agents.base_agent import BaseAgent
from app.utils.data_loader import DataLoader


class DataQualityAgent(BaseAgent):
    """Agent responsible for validating and cross-referencing conversation data with client state."""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def extract_client_info(self) -> dict:
        """
        Extract key client information from the transcript.
        Returns a dictionary of confirmed client information.
        """
        transcript = DataLoader.load_transcript()
        prompt_template = """
        Extract ONLY factual information about the client from this conversation.
        ONLY include information that is explicitly stated in the conversation.
        DO NOT make assumptions or inferences.
        
        Conversation:
        {transcript}
        
        Return a JSON object with these fields (only include fields that are explicitly mentioned):
        {{
            "Location": "explicitly stated location",
            "Marital Status": "explicitly stated marital status",
            "# of Children": "explicitly stated number of children",
            "Occupation": "explicitly stated occupation",
            "Educational Level": "explicitly stated educational level",
            "Address": "explicitly stated address",
        }}
        
        If a field is not explicitly mentioned, omit it from the JSON.
        """

        messages = [
            {
                "role": "system",
                "content": "You are a data validation expert designed to output JSON. Extract only explicitly stated facts. Do not make assumptions. Ignore unchanged information.",
            },
            {
                "role": "user",
                "content": prompt_template.format(transcript=transcript),
            },
        ]

        response = self.get_completion(
            messages, temperature=0, response_format={"type": "json_object"}
        )

        try:
            return json.loads(response)
        except json.JSONDecodeError:
            print("Error: Could not parse client information as JSON")
            return {}

    def validate_against_client_state(self, extracted_info: dict) -> list:
        """
        Cross-reference extracted information with client state data.
        Returns a list of validation results.
        """
        validation_results = []
        client_data = DataLoader.load_client_state_dict()
        if not isinstance(extracted_info, dict):
            raise ValueError("Extracted information must be a dictionary")

        for extracted_key, extracted_value in extracted_info.items():
            if extracted_key in client_data:
                client_state_value = client_data[extracted_key]
                if extracted_value not in client_state_value:
                    validation_results.append(
                        {
                            "transcript_key": extracted_key,
                            "transcript_value": extracted_value,
                            "client_state_key": extracted_key,
                            "client_state_value": client_state_value,
                        }
                    )

        return validation_results

    def generate_quality_report(self):
        """
        Generate a comprehensive quality report of the conversation data.
        Returns a list of findings in a consistent format with bullet points.
        """
        extracted_info = self.extract_client_info()
        validation_results = self.validate_against_client_state(extracted_info)

        findings = []
        for result in validation_results:
            finding = f"- During the meeting, Haris mentioned {result['transcript_key'].lower()} ({result['transcript_value']}). The agent checked the client database noting {result['client_state_key'].lower()} is {result['client_state_value']}."
            findings.append(finding)

        # If no findings, add a default message
        if not findings:
            findings.append("- No data quality issues were found in the conversation.")

        return findings

    def run(self):
        """
        Run the data quality validation process.

        Returns:
            list: List of findings in a consistent format with bullet points.
        """
        findings = self.generate_quality_report()
        return findings


if __name__ == "__main__":
    quality_agent = DataQualityAgent()
    findings = quality_agent.run()
    with open("output/data_quality_findings.json", "w") as f:
        json.dump(findings, f, indent=4)
