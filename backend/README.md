# AI-Augmented Financial Advisor System

A multi-agent system for post-meeting analysis of financial advisor-client conversations. This system analyzes meeting transcripts, client data, and product portfolios to generate structured summaries, detect emotional patterns, identify unmet needs, and recommend products.


## Overview

The system is composed of several specialized agents working together to analyze and address behavioral biases in financial advising:

1. **Data Retrieval Agent**: Fetches and indexes relevant client and product information from various sources, including historical bias patterns
2. **Data Quality Agent**: Assesses and validates the quality of input data, ensuring reliable bias analysis
3. **Meeting Notes Agent**: Creates structured summaries of the client-advisor conversation, highlighting potential bias triggers
4. **Behavioral Bias Agent**: Core agent that analyzes conversation for behavioral biases and emotional patterns, identifying:
   - Loss aversion
   - Overconfidence
   - Anchoring
   - Herding behavior
   - Recency bias
   - Confirmation bias
5. **Financial Advisor Agent**: Provides personalized financial recommendations based on the conversation, accounting for identified biases
6. **Product Portfolio Checker Agent**: Analyzes product portfolios and identifies gaps, considering bias mitigation strategies
7. **Summarization Agent**: Generates comprehensive final reports with bias analysis and mitigation recommendations
8. **Orchestrator**: Coordinates all agents and manages the analysis pipeline, ensuring bias-aware decision making


## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/financial-advisor-system.git
   cd financial-advisor-system
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```

3. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

4. Create a `.env` file with your Azure OpenAI API key:
   ```bash
   cp .env.example .env
   # Edit .env with your Azure OpenAI API key
   ```

## Data Preparation

Understanding biases is crucial for effective financial advising. Place your data files in the `data/` directory to analyze behavioral biases:
- `client_state.csv`: Client financial information and historical bias patterns
- `product_portfolio.docx`: Product catalog with bias mitigation strategies
- `transcript.m4a`: Audio recording of the meeting (or text transcript)
- `biases.csv`: Contains identified biases and emotional patterns observed during client interactions

For demo purposes, the system can run without these files by using simulated data.

## Usage

Run the system:
```bash
python main.py
```

The system will:
1. Load and index client and product data
2. Analyze the meeting transcript for behavioral biases
3. Generate a structured summary with bias insights
4. Identify unmet needs and recommend bias-aware products
5. Create a comprehensive report with bias mitigation strategies

Reports and results are saved in the `output/` directory.****

## Implementation Details

This system uses:
- Azure OpenAI GPT models for language processing and analysis
- FAISS for vector search and semantic **retrieval**

## Future Improvements

- Real-time analysis capabilities
- Integration with more financial data sources
- Multi-language support
- Custom model fine-tuning for financial domain



