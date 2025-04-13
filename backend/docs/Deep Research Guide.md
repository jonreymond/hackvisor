Deep Research Guide

Overall Topic

From GenAI to Agentic AI: Hacking the Future of Banking

⸻

Use Case Main Goal

Develop an augmenting advisor utilizing AI agents to support human financial advisors by analyzing real-time conversation transcripts and historical client data.

⸻

Use Case Description

During client-advisor interactions formatted as Q&A conversations, transcripts are recorded in real-time. An AI agent will:
	1.	Retrieve client-specific data (<client_state>) and company product offerings (<product_portfolio>) from mock databases.
	2.	Use an intelligent chunking strategy to divide extensive conversation transcripts (<transcript>) into manageable topics or sections.
	3.	Generate structured summaries for each chunk, subsequently synthesizing these into a comprehensive summary adhering to specified requirements.

The intelligent chunking is necessary because processing an hour-long transcript alongside extensive client and product data is computationally impractical.

⸻

Objectives
	•	Integrate insights from generated summaries into existing client data, updating the User Interface (UI).
	•	Recommend relevant products discussed during the interaction but not currently in the client’s portfolio.
	•	Identify further actionable insights and opportunities based on the conversation.

⸻

Summary Requirements

    •    The transcript needs to be summarized into an overview section with key points discussed and agreed upon action items that can shared with the client
    •    Certain key words or phrases need to be extracted and compared to a client database with suggestions to the Advisor for potential changes in the database or generate notes that reinforce the data in the database is still accurate.
    •    Certain key words or phrases need to be extracted that indicate the company does not offer product that address client needs

⸻

Research Topics
	•	Agentic AI
	•	Multi-Agent Systems
	•	Agentic AI Frameworks
	•	Knowledge Retrieval (Semantic Search)
	•	Speech-to-Text
	•	Structured Summarization with Prompt Engineering
	•	Contextual awareness and emotional cue detection with CoT and Self-Reflection
	•	Agentic AI Architectures
	•	Agentic AI Design Patterns
	•	Agentic AI Implementation Strategies
⸻

Technical Requirements

Cloud Infrastructure:
	•	Microsoft Azure

OpenAI Models:
	•	GPT-4o (for summarization)
	•	Whisper (for speech-to-text)