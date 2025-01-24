from phi.agent import Agent
from phi.model.groq import Groq
from dotenv import load_dotenv
from phi.model.openai import OpenAIChat
from phi.tools.duckduckgo import DuckDuckGo
from phi.tools.yfinance import YFinanceTools

load_dotenv()
web_agent = Agent(
    name = "web_agent",
    model = Groq(id = "llama-3.3-70b-versatile"),
    # model = OpenAIChat(id="gpt-4o"),
    tools= [DuckDuckGo()],
    instructions=["Always include sources"],
    show_tool_calls=True,
    markdown=True,
)
finance_agent = Agent(
    name = "finance_agent",
    model = Groq(id = "llama-3.3-70b-versatile"),
    # model = OpenAIChat(id="gpt-4o"), #Groq(id = "llama-3.3-70b-versatile"),
    tools=[
        YFinanceTools(
            stock_price = True,
            analyst_recommendations = True,
            stock_fundamentals = True)],
    show_tool_calls=True,
    markdown=True,
    instructions=["Use  Table to display the data"],
    debug_mode=True,
)
agent_team = Agent(
    model = Groq(id = "llama-3.3-70b-versatile"),
    team = [web_agent, finance_agent],
    instructions=["Always include sources", "Use  Table to display the data"],
    show_tool_calls=True,
    markdown=True,
)
agent_team.print_response("summarise and compare analyst recommendations anf fundamentals for Tsla and nvda")