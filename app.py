from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
import streamlit as st
import os
from dotenv import load_dotenv

load_dotenv()

#API keys
OPEN_AI_APIKEY=os.getenv("OPEN_AI_APIKEY")
#for langsmith
LANGCHAIN_API_KEY=os.getenv("LANGCHAIN_APIKEY")
LANGCHAIN_TRACING_V2="true"

#prompt template
prompt=ChatPromptTemplate(
    [
        ("system","You are a helpful assistant. PLease respond to user query"),
        ("user","Question:{question}"),
    ]
)

#streamlit framework
st.title('Langhchain demo with OPENAI API')
input_text=st.text_input("Search the topic you want")

#openAI LLM
llm=ChatOpenAI(model="gpt-3.5-turbo")
output_parser=StrOutputParser()

chain=prompt|llm|output_parser

if input_text:
    st.write(chain.invoke({'question':input_text}))