
from agno.agent import Agent
from agno.models.ollama import Ollama

financial_agent = Agent(
    name="Financial Agent",
    model=Ollama(id="llama3.2:3b"),
    instructions=[
        "You are an intelligent financial research assistant.",
        "Explain financial concepts clearly.",
        "Analyze financial information provided by users.",
        "Explain risks before making financial suggestions.",
        "Never invent stock prices or financial data.",
        "Distinguish facts from assumptions."
    ],
    markdown=True
)

financial_agent.print_response(
    "Explain the difference between stocks, mutual funds, and ETFs.",
    stream=True
)
