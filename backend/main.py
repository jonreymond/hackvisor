#!/usr/bin/env python3
"""
Multi-agent Financial Advisor Analysis System

This script runs a post-meeting analysis of financial advisor-client conversations.
It processes client data, product portfolio, and conversation transcript to generate
structured summaries, analysis, and recommendations.
"""

import os
import sys
from dotenv import load_dotenv
from app.agents.orchestrator import Orchestrator

load_dotenv()


def check_requirements():
    """Check if the OPENAI_API_KEY is set."""
    if not os.getenv("OPENAI_API_KEY"):
        print("ERROR: OPENAI_API_KEY is not set.")
        print(
            "Please create a .env file with your OpenAI API key or set it as an environment variable."
        )
        print("Example: OPENAI_API_KEY=your_openai_api_key_here")
        return False
    return True


def main():
    """Run the financial advisor analysis system."""
    print("Financial Advisor Post-Meeting Analysis System")
    print("=============================================")

    if not check_requirements():
        sys.exit(1)

    orchestrator = Orchestrator()
    orchestrator.run_pipeline()

    print("\nGenerating report...")
    report = orchestrator.generate_report()

    print("\nReport Preview:")
    preview_lines = report.strip().split("\n")[:10]
    for line in preview_lines:
        print(line)
    print("...")
    print("See the output directory for the full report.")


if __name__ == "__main__":
    main()
