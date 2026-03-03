import streamlit as st
from decision_engine import process_query

st.set_page_config(page_title="AccessAI", layout="centered")

st.title("AccessAI")

mode = st.selectbox(
    "Choose mode",
    ["Auto", "Cache", "Bedrock"]
)

question = st.text_input("Enter your question")

if st.button("Submit") and question:

    with st.spinner("Processing..."):
        answer, source = process_query(question, mode)

    # Show source badge
    if source == "cache":
        st.success("Answer retrieved from CACHE")
    elif source == "bedrock":
        st.info("Answer generated using BEDROCK")
    else:
        st.warning("Unknown source")

    st.markdown("---")
    st.write(answer)