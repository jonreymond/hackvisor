# Raiffeisen Agentic Advisor Assistant (AAA)

## Overview
The Raiffeisen Agentic Advisor Assistant (AAA) is designed to enhance the efficiency and effectiveness of Raiffeisen advisors during client interactions. It acts as a multi-functional AI-powered assistant throughout the client journey — from appointment tracking and data management to improving advisory quality. Key features include:

1. **Transcript Summary**  
   AAA records and transcribes client meetings. It then generates concise summaries highlighting the main discussion topics. A keyword search function helps advisors quickly navigate the transcript and pinpoint specific sections.

2. **Data Check**  
   At the end of a session, AAA cross-references client-shared information with existing personal records and suggests updates. The advisor can then easily validate or reject proposed changes.

3. **Representativeness Bias Detection**  
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
The system is composed of several specialized agents working together:

1. **Data Retrieval Agent**: Fetches and indexes relevant client and product information
2. **Dialogue Analysis Agent**: Analyzes the conversation transcript for topics, questions, and emotional cues
3. **Summarization Agent**: Creates structured summaries of the meeting
4. **Recommendation Agent**: Identifies unmet needs and suggests relevant products
5. **Orchestrator**: Coordinates the agents and generates the final report

## User Interface

The main goal of our user interface is to provide clear strucure in the Raiffeisen design. The user interface of the project provides a comprehensive assistant for advisors, featuring the following functionalities:
- Client Data Management: Displays detailed client information, including demographics, financial details, and investment preferences, with filtering capabilities.
- Transcript Analysis: Highlights keywords in the meeting conversation transcript, allowing advisors to focus on the conversation. Keywords are dynamically styled and selectable for further exploration.
- Keyword Management: Allows users to search, add, and interact with keywords, providing insights into related terms and enhancing conversation analysis.
- Meeting Summaries: Summarizes client-advisor meetings, including notes, action items, and advisor suggestions, to streamline follow-ups and decision-making.
- Interactive Layout: Features a responsive, animated column-based layout for easy navigation between client data, transcripts, and summaries.

  To run the interface yourself, you can download/fork this repo and following the instruction in the [README](./userInterface/README.md)
![AAA Demonstration](./UserInterface.gif)
