from crewai import Crew, Process
from agents import planner_agent, researcher_agent
from tasks import planning_task, research_task

# ---------- Crew Assemble ----------
research_crew = Crew(
    agents=[planner_agent, researcher_agent],
    tasks=[planning_task, research_task],
    process=Process.sequential,
    verbose=True,
)

if __name__ == "__main__":
    user_query = input("Enter your research query: ")

    result = research_crew.kickoff(inputs={"query": user_query})

    print("\n\n========== FINAL REPORT ==========\n")
    print(result)
    