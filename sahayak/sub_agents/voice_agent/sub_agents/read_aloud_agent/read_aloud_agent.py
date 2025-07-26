# read_aloud_agent.py

from google.adk.agents import Agent
from google.genai.types import GenerateContentConfig

read_aloud_agent = Agent(
    model="gemini-2.5-pro-preview-tts",
    name="read_aloud_agent",
    description="Reads any user-provided text aloud using Gemini's native audio output.",
    instruction="""
You are a voice assistant whose sole job is to read aloud any text provided by the user.
- Do not ask questions.
- Do not explain the text.
- Simply convert the input into natural, spoken language.
- Speak with clarity, friendliness, and natural pacing.
- If the input is extremely long, summarize or ask for a shorter version politely.

Always respond in audio format unless the input is empty or inappropriate.
""",
    generate_content_config=GenerateContentConfig(
        response_mime_type="text/plain",  # audio/mpeg Ensure ADK renders the response as audio
        temperature=0.3,
        top_p=0.7,
        top_k=40,
        candidate_count=1
    )
)
