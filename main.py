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

prompt_template = """You are a digital marketing and content creation expert, and you need to create one-line advertisement copy to be printed on {output_form}.
                    Your part is to create advertising copy for product: {product_name}.
                    It must contain a summary of product name: {product_name} and description: {description}.
                    Your copy must grab the reader's attention.
                    Your sentence should reflect the characteristics of the product well.
                    You must translate {product_name} into English if was entered in Korean.
                    The copy shoud be based on the {theme} mood, and final copy must be written in English and no longer than 30 characters.
                    """
prompt = PromptTemplate(template=prompt_template,
                        
                        input_variables=['output_form', 'product_name', 'theme', 'description'])


# UI 구성

st.title('광고하고 싶은 내용을 입력해주세요')

selected_item = st.radio("결과물 출력 형태", ("SNS 게시물", "전단지", "배너", "기타"))

if selected_item == "SNS 게시물":
    output_form = 'SNS 게시물' #st.write("SNS 게시물")
elif selected_item == "전단지":
    output_form = '전단지' #st.write("전단지")
elif selected_item == "배너":
    output_form = '배너' #st.write("배너")
elif selected_item == "기타":
    output_form = st.text_input('기타')


#store_name = st.text_input('가게명')
theme = st.text_input('테마')
product_name = st.text_input('상품명')
#price = st.text_input('가격')
description = st.text_input('상세설명')

llm_chain = LLMChain(prompt=prompt, llm=llm)
inputs = {'output_form': output_form, 'theme': theme, 'product_name': product_name, 'description': description}



if st.button('Submit', type='primary'):
    with st.spinner('생성 중...'):

        st.write(llm_chain.invoke(inputs))