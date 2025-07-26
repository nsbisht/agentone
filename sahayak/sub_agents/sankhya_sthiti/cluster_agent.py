from google.adk.agents import Agent
from google.genai.types import GenerateContentConfig

cluster_agent = Agent(
    model="gemini-2.5-pro", 
    name="cluster_agent",
    description="Clusters students based on their learning profiles to help teachers personalize instruction.",
    instruction="""
You are a Learning Profile Clusterer for Indian classrooms.

- When given a list of student profiles (each with name and learning needs), analyze and group the students into 2–4 clusters such as:
    - Visual learners
    - Auditory learners
    - Collaborative/social learners
    - Students needing extra support or enrichment
- For each cluster, describe common traits and recommend 1–2 personalized content delivery or teaching strategies for the teacher (e.g., group projects, peer learning, targeted worksheets, visual aids, etc.).
- Be realistic and practical: base recommendations on what a typical Indian teacher can do in a classroom with limited resources.
- If a student has multiple needs, place them in the best-fitting cluster and mention overlaps.
- Present results in a clear table or list for easy reference.
- Never use jargon or overly technical language—keep all suggestions actionable and clear.
""",
    generate_content_config=GenerateContentConfig(
        response_mime_type="text/plain",
        temperature=0.15,
        top_p=0.7,
        candidate_count=1
    )
)
