import streamlit as st
from crewai import Crew, Process
from agents import planner_agent, researcher_agent
from tasks import planning_task, research_task

# ---------- Page Setup ----------
st.set_page_config(page_title="Contemplation AI", page_icon="🔎", layout="centered")

st.title("🔎 Contemplation AI")
st.caption("Your AI research team — plans, searches, and reports.")
st.write(
    "Enter any topic and this AI agent team will plan sub-questions, "
    "search the web, and compile a clean research report for you."
)

# ---------- Input ----------
user_query = st.text_input("What do you want to research?", placeholder="e.g. Health benefits of intermittent fasting")

run_button = st.button("Run Agent", type="primary")

# ---------- Run Crew ----------
if run_button:
    if not user_query.strip():
        st.warning("Please enter a query first.")
    else:
        with st.status("Agents are working on your query...", expanded=True) as status:
            st.write("🧠 Planner Agent is breaking down your query...")

            research_crew = Crew(
                agents=[planner_agent, researcher_agent],
                tasks=[planning_task, research_task],
                process=Process.sequential,
                verbose=True,
            )

            result = research_crew.kickoff(inputs={"query": user_query})

            st.write("✅ Research complete!")
            status.update(label="Done!", state="complete", expanded=False)

        st.subheader("📄 Final Report")
        st.markdown(str(result))

        st.download_button(
            label="Download Report (Markdown)",
            data=str(result),
            file_name="research_report.md",
            mime="text/markdown",
        )
        
