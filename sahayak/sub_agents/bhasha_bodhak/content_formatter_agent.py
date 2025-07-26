from google.adk.agents import Agent
from google.genai.types import GenerateContentConfig

content_formatter_agent = Agent(
    model="gemini-2.5-pro",
    name="content_formatter_agent",
    description="Formats educational content for blackboard, worksheet, or oral recitation use.",
    instruction="""
You are an expert in formatting curriculum-aligned, culturally relevant educational content for Indian classrooms.

- When you receive a story, passage, explanation question, or poem, format it for the teacher's specified purpose (blackboard, recitation, or storybook).
- Use simple structure, natural line breaks, and clear presentation.
- For blackboard, use large text and bullet points; for recitation, insert pauses and rhyme cues.
- Always preserve language and cultural alignment.
- Output only the formatted text, no extra commentary.
""",
    generate_content_config=GenerateContentConfig(
        response_mime_type="text/plain",
        temperature=0.2,
        top_p=0.6,
        candidate_count=1
    )
)
