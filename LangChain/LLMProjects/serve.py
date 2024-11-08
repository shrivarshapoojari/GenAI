from fastapi import FastAPI
from langchain_core.prompts import ChatMessagePromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_groq import ChatGroq
from dotenv import load_dotenv
from langchain_core.messages import HumanMessage,SystemMessage
from langserve import add_routes
import os
load_dotenv()

groq_api_key = os.getenv("GROQ_API_KEY")

model=ChatGroq(model="Gemma2-9b-It", api_key=groq_api_key)

