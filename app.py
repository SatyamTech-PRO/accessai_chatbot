import streamlit as st
from decision_engine import process_query

st.set_page_config(page_title="AccessAI", layout="centered")

st.title("AccessAI")

mode = st.selectbox(
    "Choose mode",
    ["Auto", "Bedrock", "Cache"]
)

question = st.text_input("Enter your question")

if st.button("Submit"):
    if question.strip() == "":
        st.warning("Please enter a question.")
    else:
        answer, source = process_query(question, mode)

        if source == "cache":
            st.success("Mode used: cache")
        elif source == "bedrock":
            st.success("Mode used: bedrock")

        st.write(answer)