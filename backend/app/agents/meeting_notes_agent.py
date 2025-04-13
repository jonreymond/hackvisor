import os
import sys
import json

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))

from app.agents.base_agent import BaseAgent
from app.utils.data_loader import DataLoader


class MeetingNotesAgent(BaseAgent):
    """Agent responsible for creating structured summaries of the client-advisor conversation."""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def create_meeting_notes(self):
        """
        Create a structured summary with two sections: meeting notes and action items.

        Args:
            dialogue_analysis (dict): Results from the dialogue analysis agent.

        Returns:
            dict: Structured summary with two sections.
        """
        transcript = DataLoader.load_transcript()

        prompt_template = """
        Create a concise summary of the following conversation between a financial advisor and a client.
        The summary should be organized into exactly two sections as outlined below.
        
        Transcript:
        {transcript}
        
        Please provide the summary in the following format:
        
        Client/Advisor Meeting Notes
        - [Key point 1]
        - [Key point 2]
        - [Key point 3]
        
        Agreed upon action items
        - [Action item 1]
        - [Action item 2]
        
        Keep each point short and clear. Use simple bullet points without any additional formatting.
        Focus on concrete information and decisions made during the conversation.
        """

        # Format the prompt with the transcript
        formatted_prompt = prompt_template.format(transcript=transcript)

        # Create messages for the API call
        messages = [
            {
                "role": "system",
                "content": "You are a financial conversation analyst specializing in concise summaries.",
            },
            {"role": "user", "content": formatted_prompt},
        ]

        # Get structured summary from Azure OpenAI
        structured_output = self.get_completion(messages)

        # Process the output to extract sections
        sections = {}

        # Parse the sections
        if "Client/Advisor Meeting Notes" in structured_output:
            parts = structured_output.split("Client/Advisor Meeting Notes")[1].split(
                "Agreed upon action items"
            )[0]
            sections["meeting_notes"] = parts.strip()

        if "Agreed upon action items" in structured_output:
            parts = structured_output.split("Agreed upon action items")[1]
            sections["action_items"] = parts.strip()

        return sections

    def run(self):
        """
        Run the summarization agent to create a summary of the transcript.

        Args:
            summary_type (str): Type of summary to create
                ('chunks', 'structured', or 'full').

        Returns:
            dict or str: The summary results.
        """

        return self.create_meeting_notes()


if __name__ == "__main__":
    meeting_notes_agent = MeetingNotesAgent()
    meeting_notes = meeting_notes_agent.run()
    with open("output/meeting_notes_agent_output.json", "w") as f:
        json.dump(meeting_notes, f)
