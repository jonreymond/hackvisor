# AI-Augmented Financial Advisor System

A multi-agent system for post-meeting analysis of financial advisor-client conversations. This system analyzes meeting transcripts, client data, and product portfolios to generate structured summaries, detect emotional patterns, identify unmet needs, and recommend products.

## Overview

The system is composed of several specialized agents working together:

1. **Data Retrieval Agent**: Fetches and indexes relevant client and product information
2. **Dialogue Analysis Agent**: Analyzes the conversation transcript for topics, questions, and emotional cues
3. **Summarization Agent**: Creates structured summaries of the meeting
4. **Recommendation Agent**: Identifies unmet needs and suggests relevant products
5. **Orchestrator**: Coordinates the agents and generates the final report

## Requirements

- Python 3.8+
- OpenAI API key

## Installation

1. Clone this repository:
   ```
   git clone https://github.com/yourusername/financial-advisor-system.git
   cd financial-advisor-system
   ```

2. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

3. Create a `.env` file with your OpenAI API key:
   ```
   OPENAI_API_KEY=your_openai_api_key_here
   ```

## Data Preparation

Place your data files in the `data/` directory:
- `client_state.xlsx`: Client financial information
- `product_portfolio.docx`: Product catalog
- `transcript.m4a`: Audio recording of the meeting (or text transcript)

For demo purposes, the system can run without these files by using simulated data.

## Usage

Run the system:
```
python main.py
```

The system will:
1. Load and index client and product data
2. Analyze the meeting transcript
3. Generate a structured summary
4. Identify unmet needs and recommend products
5. Create a comprehensive report

Reports and results are saved in the `output/` directory.

## Output

The system generates two types of output files:
1. **JSON analysis file**: Complete analysis results in structured format
2. **Text report file**: Human-readable report with key sections:
   - Client's Goals & Questions
   - Advisor's Analysis & Recommendations
   - Action Items & Next Steps
   - Client's Reactions/Concerns
   - Unmet Financial Needs
   - Product Recommendations
   - Suggested Next Steps

## Implementation Details

This system uses:
- LangChain for agent and chain orchestration
- OpenAI GPT models for language processing
- FAISS for vector search and semantic retrieval
- Chain-of-Thought prompting for emotional analysis
- Structured summarization with prompt engineering

## Limitations

- Real audio transcription requires OpenAI Whisper (not implemented in this prototype)
- Analysis quality depends on the OpenAI model used (GPT-4 recommended)
- Simulated data is used when real data files are not available

## Future Improvements

- Implement real-time audio transcription with Whisper
- Add more sophisticated emotion detection
- Improve parsing of Excel and Word documents
- Add a web interface for viewing reports
- Fine-tune models on financial domain data
