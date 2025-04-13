import os
import sys
import json

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))

from app.agents.base_agent import BaseAgent
from app.utils.data_loader import DataLoader


class BehaviouralBiasAgent(BaseAgent):
    """Agent responsible for identifying behavioral biases in client-advisor conversations."""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def identify_biases(self):
        """
        Identify behavioral biases in the conversation.

        Returns:
            list: Identified behavioral biases.
        """
        transcript = DataLoader.load_transcript()
        biases = DataLoader.load_biases()

        biases_str = ""
        for bias in biases:
            biases_str += f"Category: {bias['category']}\n"
            biases_str += f"Bias: {bias['bias']}\n"
            biases_str += f"Description: {bias['description']}\n"
            biases_str += f"Example: {bias['examples']}\n\n"

        prompt_template = """
        Analyze the following conversation between a financial advisor and a client.
        Identify any behavioral biases exhibited by the client based on the provided bias definitions.
        
        Conversation:
        {transcript}
        
        Behavioral Biases to Look For:
        {biases}
        
        Provide 3 specific instances where the client exhibited behavioral biases (max 150 characters per bias).
        Format each finding as:
        - [Client Name] showed [bias name] when [specific behavior/statement].
        
        Example format:
        - Haris showed confirmation bias when he dismissed market data that contradicted his tech stock investment.
        - Haris showed loss aversion when he refused to sell underperforming stocks.
        
        Keep each finding clear, specific and concise.
        """

        formatted_prompt = prompt_template.format(
            transcript=transcript, biases=biases_str
        )

        messages = [
            {
                "role": "system",
                "content": "You are a behavioral finance expert analyzing client-advisor conversations for cognitive and emotional biases.",
            },
            {"role": "user", "content": formatted_prompt},
        ]

        bias_analysis = self.get_completion(messages, temperature=0.2)
        bias_list = [bias.strip() for bias in bias_analysis.split("\n") if bias.strip()]

        return bias_list

    def run(self):
        """
        Run the behavioral bias agent to identify biases in the conversation.

        Returns:
            list: The identified behavioral biases.
        """
        biases = self.identify_biases()
        return biases


if __name__ == "__main__":
    bias_agent = BehaviouralBiasAgent()
    biases = bias_agent.run()
    with open("output/behavioural_bias_agent.json", "w") as f:
        json.dump(biases, f)
