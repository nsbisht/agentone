from google.adk.agents import Agent
from . import prompt

time_table_generator_agent = Agent(
    model="gemini-2.5-pro",
    name="time_table_generator_agent",
    description="Generates weekly timetables based on class schedules, subject frequency, teacher assignments, and daily periods.",
    instruction=prompt.INSTRUCTION,
)
