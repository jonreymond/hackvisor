import os
import sys
import json

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))

from app.agents.base_agent import BaseAgent
from app.utils.data_loader import DataLoader
from app.utils.vector_store import VectorStore


class ProductPortfolioCheckerAgent(BaseAgent):
    """Agent responsible for checking product inquiries against the existing portfolio."""

    def __init__(self, *args, **kwargs):
        """Initialize the product portfolio checker agent."""
        super().__init__(*args, **kwargs)

    def extract_product_inquiries(self) -> dict:
        """
        Extract product-related inquiries from the transcript.
        Returns a dictionary of product inquiries.
        """
        transcript = DataLoader.load_transcript()
        prompt_template = """
        Extract ONLY product-related inquiries or requests from this conversation.
        Focus on specific products or services the client is asking about.
        DO NOT include general financial advice requests.
        
        Conversation:
        {transcript}
        
        Return a JSON object with these fields (only include fields that are explicitly mentioned):
        {{
            "product_inquiries": [
                {{
                    "product_type": "type of product/service inquired about",
                    "specific_need": "specific need or requirement mentioned",
                    "context": "brief context of the inquiry"
                }}
            ]
        }}
        
        If no product inquiries are mentioned, return an empty list for product_inquiries.
        """

        messages = [
            {
                "role": "system",
                "content": "You are a product portfolio expert designed to output JSON. Extract only explicit product inquiries. Do not make assumptions or general financial advice requests.",
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
            print("Error: Could not parse product inquiries as JSON")
            return {"product_inquiries": []}

    def check_against_portfolio(self, inquiries: dict) -> list:
        """
        Check product inquiries against the existing portfolio.
        Returns a list of findings about product availability.
        """
        findings = []

        product_data = DataLoader.load_product_portfolio()
        vector_store = VectorStore()
        product_vector_store = vector_store.create_or_load(
            product_data, "product_portfolio"
        )

        for inquiry in inquiries.get("product_inquiries", []):
            product_type = inquiry.get("product_type", "")
            specific_need = inquiry.get("specific_need", "")
            search_query = f"{product_type} {specific_need}"
            search_results = product_vector_store.similarity_search(search_query, k=3)

            if search_results:
                relevance_prompt = f"""
                Analyze the following product inquiry and retrieved results to determine if Raiffeisen offers a product that matches the inquiry.
                
                Inquiry: {search_query}
                
                Retrieved Results:
                {chr(10).join([f"Result {i+1}: {result.page_content}" for i, result in enumerate(search_results)])}
                
                Based on the above information, determine if Raiffeisen offers a product that matches the inquiry.
                Return ONLY one of these exact responses:
                - "EXISTS" if Raiffeisen offers a product that matches the inquiry
                - "DOES_NOT_EXIST" if Raiffeisen does not offer a product that matches the inquiry
                - "UNCLEAR" if the information is insufficient to determine
                """

                relevance_messages = [
                    {
                        "role": "system",
                        "content": "You are a product portfolio expert. Analyze product inquiries against Raiffeisen's product portfolio and determine if a matching product exists.",
                    },
                    {"role": "user", "content": relevance_prompt},
                ]

                relevance_response = (
                    self.get_completion(relevance_messages, temperature=0)
                    .strip()
                    .upper()
                )

                if relevance_response == "DOES_NOT_EXIST":
                    finding = f"- During the meeting, Haris asked whether Raiffeisen has a solution for {product_type.lower()} which does not currently exist."
                    findings.append(finding)
                elif relevance_response == "UNCLEAR":
                    finding = f"- During the meeting, Haris asked about {product_type.lower()}, but the information about this product in our portfolio is unclear."
                    findings.append(finding)

            else:
                finding = f"- During the meeting, Haris asked whether Raiffeisen has a solution for {product_type.lower()} which does not currently exist."
                findings.append(finding)

        return findings

    def generate_portfolio_report(self):
        """
        Generate a report of product inquiries and portfolio gaps.
        Returns a list of findings in a consistent format.
        """
        inquiries = self.extract_product_inquiries()
        findings = self.check_against_portfolio(inquiries)
        return findings

    def run(self):
        """
        Run the product portfolio checker process.

        Returns:
            list: List of findings about product availability and gaps.
        """
        findings = self.generate_portfolio_report()
        return findings


if __name__ == "__main__":
    portfolio_agent = ProductPortfolioCheckerAgent()
    findings = portfolio_agent.run()
    with open("output/product_portfolio_findings.json", "w") as f:
        json.dump(findings, f, indent=4)
