# ChatOpenAI configuration
import os
from langchain_openai import ChatOpenAI
from .tools import tools
from dotenv import load_dotenv

load_dotenv()

llm = ChatOpenAI(
    model="openai/gpt-oss-20b:deepinfra",
    base_url="https://router.huggingface.co/v1",
    api_key=os.getenv("HF_TOKEN"),
    temperature=0.2,
)

llm_with_tools = llm.bind_tools(tools)
