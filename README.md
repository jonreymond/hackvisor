# Raiffeisen Agentic Advisor Assistant (AAA)

The Agentic Advisor Assistant is a solution for Client Advisors to 

1) Automate manual tasks such as summarizing Client and Advisor meeting notes and action items with speech to text capabilities
2) Leverage AI agents to assess client datasets, meeting transcripts, and other reference data multiple AI agents to perform data quality checks to either validate data is correct or identify errors
3) Leverage AI agents to search for key phrases or words in meeting transcripts to identify ways to improve the Advisors recommendations to clients, identify existing products that meeting the Client’s needs, and identify Client needs that are unmet with current products. 
 
The solution is built in Microsoft Azure infrastructure leveraging Whisper for Speech to Text capabilities and GPT-4o for RAG based functions. The end user application is built in Python and is intended to provide Advisors with relevant data about the Client, meeting summaries, AI generated recommendations, and the ability to perform various actions. 

The Raiffeisen Agentic Advisor Assistant (AAA) is designed to enhance the efficiency and effectiveness of Raiffeisen advisors during client interactions. It acts as a multi-functional AI-powered assistant throughout the client journey — from appointment tracking and data management to improving advisory quality. Key features include:

1. **Transcript Summary**  
   AAA records and transcribes client meetings. It then generates concise summaries highlighting the main discussion topics. A keyword search function helps advisors quickly navigate the transcript and pinpoint specific sections.

2. **Data Check**  
   At the end of a session, AAA cross-references client-shared information with existing personal records and suggests updates. The advisor can then easily validate or reject proposed changes.

3. **Bias Detection**  
   AAA uses pattern recognition to detect all sort of biases, cognitive, conservative, bias, that may affect the advisor’s decisions or recommendations. It provides feedback to raise awareness and improve future advisory performance.

4. **History Memory**  
   Each client's historical interactions are stored and continuously updated, allowing AAA to offer contextual suggestions, detect changes over time, and assist in continuity across appointments.

## Business
The AAA aligns with Raiffeisen’s long-term vision of digitized, client-centered banking. By automating administrative tasks and enhancing decision-making awareness, advisors can focus more on building client relationships and offering high-quality financial advice. Key business impacts include:

- **Time-saving** through meeting automation  
- **Increased accuracy** of client records  
- **Improved advisory quality** via cognitive bias monitoring  
- **Stronger customer experience** with contextual memory

## AI Agents
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

## User Interface

The main goal of our user interface is to provide clear strucure in the Raiffeisen design. The user interface of the project provides a comprehensive assistant for advisors, featuring the following functionalities:
- Client Data Management: Displays detailed client information, including demographics, financial details, and investment preferences, with filtering capabilities.
- Transcript Analysis: Highlights keywords in the meeting conversation transcript, allowing advisors to focus on the conversation. Keywords are dynamically styled and selectable for further exploration.
- Keyword Management: Allows users to search, add, and interact with keywords, providing insights into related terms and enhancing conversation analysis.
- Meeting Summaries: Summarizes client-advisor meetings, including notes, action items, and advisor suggestions, to streamline follow-ups and decision-making.
- Interactive Layout: Features a responsive, animated column-based layout for easy navigation between client data, transcripts, and summaries.
  
![AAA Demonstration](./UserInterface.gif)
