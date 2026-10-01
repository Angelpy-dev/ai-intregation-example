#chatbot node

from langgraph.graph import MessagesState
from .llm import llm_with_tools


async def chatbot(state: MessagesState):
    response = await llm_with_tools.ainvoke(
        state["messages"]
    )

    return {
        "messages": [response]
    }
