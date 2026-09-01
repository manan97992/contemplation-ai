from crewai import Agent
from dotenv import load_dotenv

load_dotenv()

# ---------- Planner Agent ----------
planner_agent = Agent(
    role="Senior Research Planner",
    goal="Given a research query, break it down into 3-5 clear, specific sub-questions that together give full coverage of the topic",
    backstory=(
        "You are a meticulous research strategist. Before anyone starts "
        "searching the internet, you think carefully about what exactly "
        "needs to be found out, and split a broad topic into focused, "
        "non-overlapping sub-questions."
    ),
    verbose=True,
    allow_delegation=False,
)
from crewai_tools import TavilySearchTool

# ---------- Tavily Search Tool ----------
search_tool = TavilySearchTool()

# ---------- Researcher Agent ----------
researcher_agent = Agent(
    role="Senior Web Researcher",
    goal=(
        "Given a specific sub-question, search the web using the Tavily "
        "tool and extract accurate, relevant, and up-to-date information "
        "that directly answers it. Always prioritize credible sources and "
        "recent information over outdated or unreliable ones."
    ),
    backstory=(
        "You are an experienced online researcher who has spent years "
        "digging through search results to separate signal from noise. "
        "You never accept the first result blindly — you cross-check facts "
        "when something seems uncertain, and you always note where "
        "information came from. You are efficient: you search with "
        "precise queries rather than vague ones, and you summarize "
        "findings clearly instead of dumping raw search results."
    ),
    tools=[search_tool],
    verbose=True,
    allow_delegation=False,
)
