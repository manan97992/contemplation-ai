from crewai import Task
from agents import planner_agent, researcher_agent

# ---------- Planning Task ----------
planning_task = Task(
    description=(
        "Analyze the following research query and break it down into "
        "3-5 focused sub-questions that together give comprehensive "
        "coverage of the topic:\n\n"
        "Query: {query}"
    ),
    expected_output=(
        "A numbered list of 3-5 specific, searchable sub-questions "
        "covering the topic comprehensively, ordered from general "
        "background to specific details."
    ),
    agent=planner_agent,
)

# ---------- Research Task ----------
research_task = Task(
    description=(
        "Using the sub-questions provided by the Research Planner, search "
        "the web for accurate and up-to-date information to answer each "
        "one. Then synthesize everything into a single, well-organized "
        "research report on the original query: {query}"
    ),
    expected_output=(
        "A clear, well-structured report in markdown format with headings "
        "for each sub-topic, covering all sub-questions with accurate, "
        "sourced information. End with a brief summary section."
    ),
    agent=researcher_agent,
    context=[planning_task],
)
