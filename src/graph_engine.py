import json
from typing import TypedDict  #Helps define a structured state (like a schema)
from langgraph.graph import StateGraph  #to build a workflow


class State(TypedDict): #what data flows through the graph
    bot_id: str
    persona: str
    topic: str
    context: list


def mock_searxng_search(query: str): #Simulates a search engine
    if "AI" in query:
        return ["OpenAI launches a powerful new model"] #If topic is AI → return related news
    elif "crypto" in query:
        return ["Bitcoin hits new all-time high"]
    else:
        return ["Tech industry evolving rapidly"]


def decide_topic(state: State):
    print("STATE RECEIVED:", state)  #Debug: shows incoming data

    topic = "AI"

    print("Node1: Topic ->", topic)
    return {"topic": topic} #Returns new data → added to state


def web_search(state: State):
    results = mock_searxng_search(state["topic"]) #Uses topic from previous step

    print("Node2: Search Results ->", results)
    return {"context": results}


# -------- NODE 3 --------
def generate_post(state: State):
    persona = state["persona"]

    if "destroying society" in persona.lower():
        tone = "This is concerning and highlights deeper risks of technology."
    elif "finance" in persona.lower():
        tone = "This could significantly impact markets and ROI."
    else:
        tone = "This proves technology is advancing rapidly."

    output = {
        "bot_id": state["bot_id"],
        "topic": state["topic"],
        "post_content": f"{state['context'][0]}. {tone} #{state['bot_id']}"
    }

    print("Node3: Generated JSON")
    print(json.dumps(output))

    return output


# -------- BUILD GRAPH --------
def build_graph():
    graph = StateGraph(State)

    graph.add_node("decide", decide_topic)
    graph.add_node("search", web_search)
    graph.add_node("generate", generate_post)

    graph.set_entry_point("decide")
    graph.add_edge("decide", "search")
    graph.add_edge("search", "generate")

    return graph.compile()