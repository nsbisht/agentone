# AgentOne

This repository contains the code for **Sahayak**, an AI agent developed as part of Google Cloud's Agentic AI Day Hackathon. Sahayak is designed to assist teachers in India by providing tools for content creation, lesson planning, assessment generation, and more, with a focus on local relevance and accessibility.

## Repository Structure

The core of this repository is the `sahayak` directory, which houses the code for the Sahayak agent and its various sub-agents. The other directories (`gyaan_aadhar`, `multi_tool_agent`, `travel_concierge`) were primarily used for experimentation during development.

Here is a high-level overview of the relevant repository structure:

```
.
├── README.md
├── deploy.sh
├── sahayak
│   ├── __init__.py
│   ├── requirements.txt
│   ├── sahayak.py
│   └── sub_agents
│       ├── __init__.py
│       ├── bhasha_bodhak
│       │   ├── __init__.py
│       │   ├── bhasha_bodhak.py
│       │   ├── content_formatter_agent.py
│       │   └── rag_agent.py
│       ├── chitra_patra
│       │   ├── __init__.py
│       │   ├── chitra_patra.py
│       │   └── sub_agents
│       │       ├── __init__.py
│       │       ├── diagram_creator_agent.py
│       │       ├── upload_image_agent.py
│       │       └── worksheet_generator_agent.py
│       ├── jigyasa_samadhan
│       │   ├── __init__.py
│       │   └── agent.py
│       ├── samay_sutra
│       │   ├── __init__.py
│       │   ├── agent.py
│       │   └── sub_agents
│       │       ├── __init__.py
│       │       ├── filler_agent
│       │       │   ├── __init__.py
│       │       │   └── agent.py
│       │       ├── schedule_validator
│       │       │   ├── __init__.py
│       │       │   └── agent.py
│       │       └── time_table_generator
│       │           ├── __init__.py
│       │           ├── agent.py
│       │           └── prompt.py
│       ├── sankhya_sthiti
│       │   ├── __init__.py
│       │   ├── agent.py
│       │   ├── cluster_agent.py
│       │   └── seating_profiles.py
│       └── varg_vimarsh  # Assuming this should be here based on your description
│           ├── __init__.py
│           └── agent.py
├── .idx
│   ├── dev.nix
│   └── integrations.json
├── Dockerfile
├── Procfile
├── env.sample
├── pyproject.toml
└── uv.lock
```

## Sahayak Agent: Features and Capabilities

The Sahayak agent offers a suite of tools to empower teachers:

*   **Bhasha Bodhak (Hyper-Local Content Creator):** Enables teachers to request culturally rooted content in local languages. Sahayak generates simple, curriculum-aligned material using Gemini and Gemma Multimodal Models.
*   **Path Karyashala (Lesson & Game Planner):** Auto-generates weekly lesson plans and interactive learning games based on syllabus topics, designed for diverse ability groups.
*   **Prashn Manthan (Adaptive Exam Paper Generator):** Automatically sets exam papers with topic-based, difficulty-balanced questions. Adapts to class performance trends and includes moral/contextual reasoning-based questions.
*   **Chitra Patra (Smart Visual & Worksheet Maker):** Allows uploading textbook photos and can generate worksheets for multiple grade levels, including blackboard-friendly diagrams.
*   **Jigyasa Samadhan (Instant Knowledge Base):** Provides simple, accurate answers to spontaneous student questions in the local language with relatable analogies.
*   **Vachan Sahayak (Audio & Assessment Assistant):** Uses Vertex AI’s Speech-to-Text AI capability to read poems/passages aloud, supporting oral skills evaluation.
*   **Agni Pariksha (Offline Readiness):** Deployed with offline-ready support for rural classrooms with low or no connectivity using Gemma multimodal Models.
*   **Samay Sutra (Smart Student Timetable Planner):** Creates personalized student timetables ensuring balanced study periods, regular breaks, and mindfulness time.
*   **Sankhya Sthiti (Smart Seating Manager):** Creates optimized seating charts for daily classes or exams, considering learning needs and fairness.
*   **Varg Vimarsh (Student Cluster Mapper):** Clusters students using embedding-based learning profiles to personalize content delivery, using Vertex AI models for grouping.
*   **Gyaan Aadhar (Grounded Knowledge Core):** Ingests educational materials (like NCERT books, exam papers) to ensure grounded, syllabus-aligned answers and resources.

## Deployment

The Sahayak agent is deployed to Google Cloud Run using the `deploy.sh` script. This script automates the deployment process using the Agent Development Kit (ADK) and Google Cloud SDK.

The high-level deployment steps are as follows:

1.  **Authentication:** Authenticate with Google Cloud using `gcloud auth login`.
2.  **Project Configuration:** Set the Google Cloud project and location.
3.  **ADK Deployment:** Utilize the `uv run adk deploy cloud_run` command to package and deploy the agent to Cloud Run.
4.  **Building and Deploying:** The process builds a container image from the agent code and deploys it as a new revision on Cloud Run.
5.  **Service URL:** The deployed agent becomes accessible via a generated service URL.

## Interacting with Sahayak

You can interact with the Sahayak agent at the following URL:

https://sahayak-531697556153.us-central1.run.app/dev-ui/?app=sahayak

This agent demonstrates the capabilities developed during the hackathon and the practical application of agentic AI in an educational context.
