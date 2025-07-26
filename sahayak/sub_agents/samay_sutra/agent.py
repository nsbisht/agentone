# samay_sutra/timetable_coordinator.py

from google.adk.agents import SequentialAgent
from .sub_agents.time_table_generator.agent import time_table_generator_agent
from .sub_agents.schedule_validator.agent import schedule_validator_agent
from .sub_agents.filler_agent.agent import filler_agent

timetable_coordinator = SequentialAgent(
    name="timetable_coordinator",
    description="Coordinates generation, validation, and enhancement of the school timetable.",
    sub_agents=[
        time_table_generator_agent,
        schedule_validator_agent,
        filler_agent
    ]
)

root_agent = timetable_coordinator
