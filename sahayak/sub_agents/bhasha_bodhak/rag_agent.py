import os
from google.adk.agents import Agent
from google.adk.tools.retrieval.vertex_ai_rag_retrieval import VertexAiRagRetrieval
from vertexai.preview import rag
from google.genai.types import GenerateContentConfig

ask_vertex_retrieval = VertexAiRagRetrieval(
    name='retrieve_rag_documentation',
    description='Use this tool to retrieve culturally-rooted, curriculum-aligned content from the RAG corpus.',
    rag_resources=[
        rag.RagResource(
            rag_corpus="projects/agentone-466906/locations/us-central1/ragCorpora/6917529027641081856"
        )
    ],
    similarity_top_k=8,
    vector_distance_threshold=0.6,
)

ask_vertex_search = VertexAiRagRetrieval(
    name='search',  # <-- This is the key change!
    description='Use this tool to retrieve culturally-rooted, curriculum-aligned content from the RAG corpus for the requested local language and topic.',
    rag_resources=[
        rag.RagResource(
            rag_corpus="projects/agentone-466906/locations/us-central1/ragCorpora/6917529027641081856"
        )
    ],
    similarity_top_k=8,
    vector_distance_threshold=0.6,
)


rag_retrieval_agent = Agent(
    model='gemini-2.5-flash',
    name='rag_retrieval_agent',
    description="Fetches relevant local-language curriculum content from the RAG corpus.",
    instruction="""
You are an advanced RAG agent for Indian education.

- When given a topic, class, and language, use the RAG retrieval tool to fetch relevant content.
- Summarize or adapt what you find for the student's grade and local context.
- If the query is missing grade or language, ask the user for this information.
- Output only the content, ready for further formatting or use.
""",
    tools=[ask_vertex_retrieval,ask_vertex_search],
    generate_content_config=GenerateContentConfig(
        response_mime_type="text/plain",
        temperature=0.3,
        top_p=0.7,
        candidate_count=1
    )
)
