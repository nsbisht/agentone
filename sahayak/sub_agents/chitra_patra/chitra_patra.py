from google.adk.agents import Agent
from .sub_agents import (
    upload_image_agent,
    worksheet_generator_agent,
    diagram_creator_agent,
)

chitra_patra_agent = Agent(
    model="gemini-2.5-pro",
    name="chitra_patra",
    description="Smart Visual & Worksheet Maker: Upload textbook images, generate worksheets, and create blackboard-friendly diagrams for any grade.",
    instruction="""
You are Chitra Patra—the smart assistant for Indian teachers.
- Guide users to upload textbook images or blackboard photos using the upload agent.
- After images are uploaded, let users choose between generating a worksheet or extracting a diagram.
- Route worksheet requests to the worksheet generator agent, and diagram/visual requests to the diagram creator agent.
- For ambiguous queries, ask clarifying questions: "Do you want to generate a worksheet, create a diagram, or just upload content?"
- Always give friendly, step-by-step instructions and confirmations for each stage.
""",
    sub_agents=[
        upload_image_agent,
        worksheet_generator_agent,
        diagram_creator_agent,
    ]
)

root_agent = chitra_patra_agent
