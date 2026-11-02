
from agno.agent import Agent
from agno.models.ollama import Ollama
from agno.os import AgentOS
from agno.tools.yfinance import YFinanceTools

# Financial market data tools
finance_tools = YFinanceTools(
    enable_company_info=True,
    enable_stock_fundamentals=True,
    enable_historical_prices=True,
    enable_key_financial_ratios=True,
    enable_company_news=True,
)

# Create Financial Agent
financial_agent = Agent(
    name="Financial Agent",
    model=Ollama(
        id="llama3.2:3b",
        host="http://localhost:11434"
    ),
    tools=[finance_tools],
    instructions=[
        "You are an intelligent financial research assistant.",
        "Use Yahoo Finance tools to retrieve stock market data.",
        "Always use tools when users ask for current stock prices.",
        "Never invent stock prices, financial metrics or news.",
        "Clearly distinguish retrieved facts from your analysis.",
        "Use tables when comparing stocks.",
        "Explain investment risks.",
        "Do not provide personalized financial advice."
    ],
    add_datetime_to_context=True,
    markdown=True
)

# Start AgentOS
agent_os = AgentOS(agents=[financial_agent])

app = agent_os.get_app()
