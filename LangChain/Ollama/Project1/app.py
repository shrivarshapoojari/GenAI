import os
from dotenv import load_dotenv
from langchain_community.llms import Ollama
import streamlit as  st
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

 
 
os.environ["LANGCHAIN_API_KEY"]=os.getenv("LANGCHAIN_API_KEY")
os.environ["LANGCHAIN_TRACING_V2"]="true"
os.environ["LANGCHAIN_PROJECT"]=os.getenv("LANGCHAIN_PROJECT")



prompt=ChatPromptTemplate.from_messages(
[

    ("system","You are a helpful assistant please respond to the questions asked"),
    ("user","Question{question}")
])




st.title("Ollama Chatbot")
input_text=st.text_input("Ask your question here")


llm=Ollama(model="llama3")

output_parser=StrOutputParser()
chain= prompt|llm|output_parser

if  input_text:
    st.write(chain.invoke({"question":input_text}))
