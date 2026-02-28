import streamlit as st
from decision_engine import process_query

st.set_page_config(page_title="AccessAI", layout="centered")

st.title("AccessAI")

mode = st.selectbox(
    "Choose mode",
    ["Auto", "bharat", "general"]
)

question = st.text_input("Enter your question")

if st.button("Submit"):
    if not question.strip():
        st.warning("Please enter a question.")
    else:
        with st.spinner("Thinking..."):
            answer, final_mode = process_query(question, mode)

        st.success(f"Mode used: {final_mode}")
        st.write(answer)