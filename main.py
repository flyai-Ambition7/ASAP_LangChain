from dotenv import load_dotenv
from openai import OpenAI
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
from langchain_openai import OpenAI
import os
import streamlit as st

load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")


template = """Question: {question}

Answer: Let's think step by step."""

prompt = PromptTemplate.from_template(template)
llm = OpenAI(model_name="gpt-3.5-turbo-instruct")

llm_chain = LLMChain(prompt=prompt, llm=llm)

question = "make one line advertisement text about coffee in korean"

st.text_input('설명')

if st.button('Submit', type='primary'):
    with st.spinner('생성 중...'):
        st.write(llm_chain.invoke(question))