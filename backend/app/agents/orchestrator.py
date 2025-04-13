import json
import os
import sys
from datetime import datetime

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))

from app.agents.data_retrieval_agent import DataRetrievalAgent
from app.agents.meeting_notes_agent import MeetingNotesAgent
from app.agents.summarization_agent import SummarizationAgent
from app.agents.behavioural_bias_agent import BehaviouralBiasAgent
from app.agents.data_quality_agent import DataQualityAgent
from app.agents.financial_advisor_agent import FinancialAdvisorAgent
from app.agents.product_portfolio_checker_agent import ProductPortfolioCheckerAgent
from config.config import OUTPUT_DIR


class Orchestrator:
    """Coordinates all agents to process a client-advisor conversation."""

    def __init__(self):
        """Initialize the orchestrator with all required agents."""
        self.data_retrieval_agent = DataRetrievalAgent()

    def save_results(self, results):
        """
        Save results to txt file.

        Args:
            results (dict): Results from all agents.
        """
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"meeting_analysis_{timestamp}.md"
        filepath = os.path.join(OUTPUT_DIR, filename)

        try:
            with open(filepath, "w") as f:
                f.write(results)
            print(f"\nResults saved to {filepath}")
        except Exception as e:
            print(f"Error saving results: {e}")

    def run(self):
        """
        Run the full pipeline to process the conversation.

        Returns:
            dict: Results from all agents.
        """
        behavioural_bias_summary = BehaviouralBiasAgent().run()
        data_quality_check = DataQualityAgent().run()
        product_portfolio_check = ProductPortfolioCheckerAgent().run()
        financial_advises = FinancialAdvisorAgent().run()
        meeting_notes = MeetingNotesAgent().run()
        summary = SummarizationAgent().run(
            behavioural_bias_summary,
            data_quality_check,
            product_portfolio_check,
            financial_advises,
            meeting_notes,
        )
        self.save_results(summary)


if __name__ == "__main__":
    orchestrator = Orchestrator()
    orchestrator.run()
