from fastapi import APIRouter

from agent.graph import agent
from schemas.chat import ChatRequest, ChatResponse


router = APIRouter()


@router.post("/chat", response_model=ChatResponse)
async def chat(request: ChatRequest):

    result = await agent.ainvoke({
        "messages": [
            {
                "role": "user",
                "content": request.message
            }
        ]
    })

    response = result["messages"][-1].content

    return ChatResponse(
        response=response
    )
