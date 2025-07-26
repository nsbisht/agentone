from google.adk.agents import Agent
from .sub_agents.voice_agent import voice_agent
from .sub_agents.chitra_patra import chitra_patra

sahayak_agent = Agent(
    model="gemini-2.5-pro",
    name="sahayak",
    description="Sahayak: An AI-powered assistant for teachers. Automatically routes requests to the right specialized agent: voice, visual worksheet, or future assistants.",
    instruction="""
You are Sahayak, an AI-powered assistant for teachers in Indian classrooms.
- Your job is to understand the user's request and route it to the correct sub-agent.
- If the query is about reading aloud, pronouncing text, or speech, route it to the voice_agent.
- If it is about worksheet creation, image upload, or diagram generation, route it to chitra_patra.
- If a new specialized agent is added, match based on intent, keywords, or explicit user instructions.
- For ambiguous queries, politely ask the user to clarify what they want to do.
- Always reply in a concise, clear, teacher-friendly way.
""",
    sub_agents=[
        voice_agent,
        chitra_patra,
        # Add new agent variables here as you expand Sahayak
    ]
)

root_agent = sahayak_agent
