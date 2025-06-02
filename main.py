import streamlit as st
import pandas as pd
import os
from Cleaner.data_cleaner import clean_dataset
# from llm.chat_agent import DefaultLLMAgent
from llm.chat_agent import ChatLLM
from llm.data_analyst_agent import DataAnalystAgent

# agent = DefaultLLMAgent()

st.set_page_config(page_title="Dataset Analyzer")
st.title("Upload your dataset")

data_dir = "uploads"
os.makedirs(data_dir, exist_ok=True)
csv_path = os.path.join(data_dir, "uploaded_data.csv")

uploaded_file = st.file_uploader("Upload CSV file", type="csv")

if uploaded_file is not None:
    with open(csv_path, "wb") as f:
        f.write(uploaded_file.getbuffer())
    st.success(f"File saved to `{csv_path}`")

if os.path.exists(csv_path):
    df = pd.read_csv(csv_path)
    st.subheader("Data:")
    st.dataframe(df, use_container_width=True)
else:
    st.info("Upload a CSV file to begin.")

if st.button("Clean Dataset (LLM)"):
    if os.path.exists(csv_path):
        df = pd.read_csv(csv_path)
        df = clean_dataset(df, 'llm')
        st.subheader("Data Read from File:")
        st.dataframe(df, use_container_width=True)
    else:
        st.warning("No CSV file found in the data folder.")

if st.button("Clean Dataset (static)"):
    if os.path.exists(csv_path):
        df = pd.read_csv(csv_path)
        df = clean_dataset(df, 'static')
        st.subheader("Data Read from File:")
        st.dataframe(df, use_container_width=True)
    else:
        st.warning("No CSV file found in the data folder.")


### Chat bot
st.title("Dataset Analyzer")
st.write("Ask me anything about your dataset!")

if "messages" not in st.session_state:
    st.session_state.messages = []

for msg in st.session_state.messages[1:]:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

user_input = st.chat_input("Type your message...")

if user_input:
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.markdown(user_input)

    with st.chat_message("assistant"):
        reply = DataAnalystAgent.run(st.session_state.messages)
        
        st.markdown(reply)

    st.session_state.messages.append({"role": "assistant", "content": reply})



   