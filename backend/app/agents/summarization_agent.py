import os
import sys
import json

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))

from app.agents.base_agent import BaseAgent
from app.utils.data_loader import DataLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from config.config import CHUNK_SIZE, CHUNK_OVERLAP


class SummarizationAgent(BaseAgent):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def create_structured_summary(
        self,
        behavioural_bias_summary,
        data_quality_check,
        product_portfolio_check,
        financial_advises,
        meeting_notes,
    ):
        """
        Create a structured markdown summary with two sections:
        1. Meeting Notes
        2. Advisor Suggestions (including behavioral biases, data quality, product portfolio, and financial advice)

        Args:
            behavioural_bias_summary (list): List of identified behavioral biases
            data_quality_check (list): List of data quality findings
            product_portfolio_check (list): List of product portfolio findings
            financial_advises (list): List of financial advisor recommendations
            meeting_notes (dict): Dictionary containing meeting notes and action items

        Returns:
            str: Formatted markdown summary
        """
        # Format meeting notes section
        meeting_notes_section = "# Meeting Notes\n\n"

        # Add meeting notes if available
        if meeting_notes and "meeting_notes" in meeting_notes:
            meeting_notes_section += meeting_notes["meeting_notes"] + "\n\n"

        # Add action items if available
        if meeting_notes and "action_items" in meeting_notes:
            meeting_notes_section += (
                "## Action Items\n\n" + meeting_notes["action_items"] + "\n\n"
            )

        # Format advisor suggestions section
        advisor_suggestions_section = "# Advisor Suggestions\n\n"

        # Add behavioral biases if available
        if behavioural_bias_summary:
            advisor_suggestions_section += "## Behavioral Biases\n\n"
            for bias in behavioural_bias_summary:
                advisor_suggestions_section += bias + "\n"
            advisor_suggestions_section += "\n"

        # Add data quality findings if available
        if data_quality_check:
            advisor_suggestions_section += "## Data Quality\n\n"
            for finding in data_quality_check:
                advisor_suggestions_section += finding + "\n"
            advisor_suggestions_section += "\n"

        # Add product portfolio findings if available
        if product_portfolio_check:
            advisor_suggestions_section += "## Product Portfolio\n\n"
            for finding in product_portfolio_check:
                advisor_suggestions_section += finding + "\n"
            advisor_suggestions_section += "\n"

        # Add financial advisor recommendations if available
        if financial_advises:
            advisor_suggestions_section += "## Financial Recommendations\n\n"
            for recommendation in financial_advises:
                advisor_suggestions_section += recommendation + "\n"
            advisor_suggestions_section += "\n"

        # Combine both sections
        markdown_summary = meeting_notes_section + advisor_suggestions_section

        return markdown_summary

    def run(
        self,
        behavioural_bias_summary,
        data_quality_check,
        product_portfolio_check,
        financial_advises,
        meeting_notes,
    ):
        """
        Run the summarization agent to create a structured markdown summary.

        Args:
            behavioural_bias_summary (list): List of identified behavioral biases
            data_quality_check (list): List of data quality findings
            product_portfolio_check (list): List of product portfolio findings
            financial_advises (list): List of financial advisor recommendations
            meeting_notes (dict): Dictionary containing meeting notes and action items

        Returns:
            str: Formatted markdown summary
        """
        return self.create_structured_summary(
            behavioural_bias_summary,
            data_quality_check,
            product_portfolio_check,
            financial_advises,
            meeting_notes,
        )


if __name__ == "__main__":
    summarization_agent = SummarizationAgent()
    summary = summarization_agent.run()
    with open("output/summarization_agent_output.json", "w") as f:
        json.dump(summary, f)
