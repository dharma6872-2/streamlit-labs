import streamlit as st
import openai

# OpenAI API 키 설정
openai.api_key = "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"

# Streamlit 앱의 제목을 설정합니다.
st.title("대화형 챗봇")

# 사용자에게 질문을 입력받습니다.
user_input = st.text_input("질문을 입력하세요:")

# 사용자가 질문을 입력한 경우에만 챗봇의 응답을 생성합니다.
if user_input:
    # OpenAI API를 사용하여 챗봇의 응답을 생성합니다.
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=user_input,
        max_tokens=500,
        temperature=0.7
    )

    # 챗봇의 응답을 출력합니다.
    bot_response = response['choices'][0]['text'].strip()
    st.text("챗봇 응답: " + bot_response)
