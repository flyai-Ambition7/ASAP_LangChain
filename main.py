from dotenv import load_dotenv
#from openai import OpenAI
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
from langchain_openai import OpenAI
import os
import streamlit as st

load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

llm = OpenAI(model_name="gpt-3.5-turbo-instruct")

store_name = 'abc마트'
purpose = ''
result_type = ''
theme = '밝은 분위기'


product_name = '운동화'
price='15000'
description = '검은색 신발 초등학생한테 인기 많음'
business_hours = ''
location = ''
contact = ''



prompt_template = """I want you to act as a copywriter for people, you must make a one line advertising text in korean for sns contents and use these reference information
                    first, our store name is {sn}, I want to make these text in {th} mood, I want to advertise this {pn} and this is our products feature : {ds}"""

'''template = """Question: {question}

Answer: Let's think step by step."""'''

prompt = PromptTemplate(template=prompt_template,
                        input_variables=['sn', 'th', 'pn', 'ds'])



store_name = st.text_input('가게명')
theme = st.text_input('테마')
product_name = st.text_input('상품명')
description = st.text_input('상세설명')

llm_chain = LLMChain(prompt=prompt, llm=llm)
inputs = {'sn': store_name, 'th': theme, 'pn': product_name, 'ds': description}



if st.button('Submit', type='primary'):
    with st.spinner('생성 중...'):

        st.write(llm_chain.invoke(inputs))