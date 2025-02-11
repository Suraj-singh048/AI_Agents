from phi.agent import Agent
from phi.model.groq import Groq
from dotenv import load_dotenv
from phi.model.openai import OpenAIChat
from phi.tools.yfinance import YFinanceTools

load_dotenv()
agent = Agent(
    # model = Groq(id = "llama-3.3-70b-versatile"),
    model = OpenAIChat(id="gpt-4o"), #Groq(id = "llama-3.3-70b-versatile"),
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

agent.print_response("summarise and compare analyst recommendations anf fundamentals for Tsla and nvda")