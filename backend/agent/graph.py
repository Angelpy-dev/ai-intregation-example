#LangGraph construction
from langgraph.graph import StateGraph, MessagesState, START
from langgraph.prebuilt import ToolNode, tools_condition

from .nodes import chatbot
from .tools import tools


def build_graph():

    graph = StateGraph(MessagesState)

    graph.add_node("chatbot", chatbot)
    graph.add_node("tools", ToolNode(tools))

    graph.add_edge(START, "chatbot")

    graph.add_conditional_edges(
        "chatbot",
        tools_condition
    )

    graph.add_edge("tools", "chatbot")

    return graph.compile()


agent = build_graph()
