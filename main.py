from dotenv import load_dotenv
from openai import OpenAI
from langchain_community.llms import openai
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
from langchain_openai import OpenAI
import os
import httpx


load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")


template = """Question: {question}

Answer: Let's think step by step."""

prompt = PromptTemplate.from_template(template)
llm = OpenAI(model_name="gpt-3.5-turbo-instruct")

llm_chain = LLMChain(prompt=prompt, llm=llm)

question = "What NFL team won the Super Bowl in the year Justin Beiber was born?"

print(llm_chain.invoke(question))
