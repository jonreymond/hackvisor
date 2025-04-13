import json
import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))


from app.agents.base_agent import BaseAgent
from app.utils.data_loader import DataLoader
from app.agents.data_retrieval_agent import DataRetrievalAgent


class FinancialAdvisorAgent(BaseAgent):
    """Agent responsible for providing financial advisor recommendations based on the conversation."""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def generate_recommendations(self, client_data):
        """
        Generate financial advisor recommendations based on the conversation.

        Args:
            client_data (dict): Client information from data retrieval.

        Returns:
            list: Financial advisor recommendations.
        """
        client_data_str = (
            "\n".join([f"{k}: {v}" for k, v in client_data.items()])
            if isinstance(client_data, dict)
            else client_data
        )

        prompt_template = """
        Based on the following conversation between a financial advisor and a client, provide 3 specific and short (max 150 characters) recommendations for the advisor. Focus on life events, portfolio adjustments, and necessary actions.
        
        Client Information:
        {client_data}
        
        Provide recommendations in the following format:
        - [Client Name] mentioned [life event/concern]. Advisor should [action].
        
        Example format:
        - During the meeting, Haris mentioned a significant life event (buying a house). The Advisor should consider updating the portfolio allocation to generate liquidity to purchase a house.
        - During the meeting, Haris mentioned a significant life event (having a baby). The Advisor should consider updating the portfolio allocation.
        
        Keep each recommendation clear, specific, and actionable. Focus on concrete steps the advisor should take.
        """

        # Format the prompt with the client data, topics, and emotional insights
        formatted_prompt = prompt_template.format(
            client_data=client_data_str,
        )

        messages = [
            {
                "role": "system",
                "content": "You are a financial advisor providing specific recommendations based on client conversations.",
            },
            {"role": "user", "content": formatted_prompt},
        ]

        recommendations = self.get_completion(messages, temperature=0.2)
        recommendation_list = [
            rec.strip() for rec in recommendations.split("\n") if rec.strip()
        ]

        return recommendation_list

    def run(self):
        """
        Run the financial advisor agent to generate recommendations.

        Returns:
            list: The financial advisor recommendations.
        """
        data_retrieval_agent = DataRetrievalAgent()
        client_data = data_retrieval_agent.run(
            "client", "client profile and financial situation"
        )

        print("Generating financial advisor recommendations...")
        recommendations = self.generate_recommendations(
            client_data["summary"] if isinstance(client_data, dict) else client_data,
        )

        return recommendations


if __name__ == "__main__":
    recommendation_agent = FinancialAdvisorAgent()
    recommendations = recommendation_agent.run()
    with open("output/financial_advisor_agent.json", "w") as f:
        json.dump(recommendations, f)
