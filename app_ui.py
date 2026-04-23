import streamlit as st
from app import process_command

st.set_page_config(page_title="Automotive AI Assistant", page_icon="🚗")

st.title("🚗 Context-Aware Automotive AI Assistant")
st.write("Intent + Entity + Action pipeline")

user_input = st.text_input("Enter your command:")

if st.button("Process Command"):
    if user_input:
        result = process_command(user_input)

        st.subheader("🔍 Results")
        st.success(f"Intent: {result['intent']}")
        st.info(f"Confidence: {result['confidence']}%")

        st.subheader("📦 Extracted Entities")
        st.write(result["entities"])

        st.subheader("⚙️ Action")
        st.write(result["action"])
    else:
        st.warning("Please enter a command")
