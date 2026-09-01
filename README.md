# 🔎 Contemplation AI

**An autonomous multi-agent research assistant.** Give it any topic — it plans the research, searches the web, and compiles a clean, sourced report. No manual digging required.

🔗 **Live app:** [contemplation-ai.streamlit.app](https://contemplation-ai.streamlit.app)

---

## What it does

1. You enter a research topic.
2. A **Planner Agent** breaks it down into 3–5 focused sub-questions.
3. A **Researcher Agent** searches the web (via Tavily) for each sub-question.
4. Everything is synthesized into a single, well-organized report — with sources, ready to read or download.

## Why I built this

Manual research means opening a dozen tabs, cross-checking sources, and stitching notes together by hand. This project automates that entire loop using a coordinated team of AI agents, inspired by planner→action→synthesis patterns used in autonomous research systems.

## Tech Stack

| Layer | Tool |
|---|---|
| Multi-agent orchestration | [CrewAI](https://www.crewai.com/) |
| LLM | OpenAI (GPT-4o-mini) |
| Web search | [Tavily API](https://tavily.com/) |
| Frontend | [Streamlit](https://streamlit.io/) |
| Hosting | Streamlit Community Cloud |

## Run it locally

```bash
git clone https://github.com/manan97992/contemplation-ai.git
cd contemplation-ai
python -m venv venv
venv\Scripts\activate        # Windows
pip install -r requirements.txt
```

Create a `.env` file in the project root with: