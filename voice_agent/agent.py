from google.adk.agents import Agent
from google.genai.types import GenerateContentConfig
from .sub_agents.read_aloud_agent import read_aloud_agent

coordinator = Agent(
    model="gemini-2.5-pro-preview-tts",
    name="coordinator",
    description="Main router agent that delegates speech input to read_aloud_agent.",
    instruction="""
You are the root controller agent.
If the user input is non-empty, route it to the `read_aloud_agent` to speak it aloud.
If the input is empty or invalid, return nothing.
""",
    sub_agents=[read_aloud_agent],
    generate_content_config=GenerateContentConfig(
        response_mime_type="text/plain",
        temperature=0.3,
        top_p=0.7
    )
)

root_agent= coordinator