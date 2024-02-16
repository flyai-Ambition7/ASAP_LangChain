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

prompt_template = """넌 디지털 마케팅과 컨텐츠 제작 전문가로, {output_form}에 포함될 짧은 광고 문구를 만들어내야해.
                    너의 임무는 {store_name}이라는 가게에서 판매하는 {product_name}에 대한 광고 문구를 만드는 거야. 
                    상품명인 {product_name}과 가격을 의미하는 {price}, 그리고 상품에 대한 설명인{description}을 요약해서 반드시 포함해야 돼.
                    너의 대답은 독자의 관심을 끌 수 있는 강력한 헤드라인과 후킹 문구가 있어야해.
                    최종 문구는 {theme} 분위기를 반영해서 메인 문구는 20자 이내로 답을 작성해줘.
                    메인 문구에는 강력한 헤드라인을 만들어주고, 상세 정보는 서브 문구에 분리해줘
                    메인 문구와 서브 문구는 내용이 중복되지 않게 서로 다른 문장으로 분리해주고, 최종 시안은 3가지 버전으로 만들어줘"""

prompt = PromptTemplate(template=prompt_template,
                        
                        input_variables=['output_form', 'store_name', 'product_name', 'theme', 'price','description'])


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


store_name = st.text_input('가게명')
theme = st.text_input('테마')
product_name = st.text_input('상품명')
price = st.text_input('가격')
description = st.text_input('상세설명')

llm_chain = LLMChain(prompt=prompt, llm=llm)
inputs = {'output_form': output_form, 'store_name': store_name, 'theme': theme, 'product_name': product_name, 'price': price,'description': description}



if st.button('Submit', type='primary'):
    with st.spinner('생성 중...'):

        st.write(llm_chain.invoke(inputs))