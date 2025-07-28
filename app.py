import os
import streamlit as st
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import Runnable

# Load the GROQ API key from .env
load_dotenv()
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

# Initialize the GROQ LLM
llm = ChatGroq(
    groq_api_key=GROQ_API_KEY,
    model_name="llama3-70b-8192"  # You can change to mixtral etc.
)

# Prompt template
prompt = ChatPromptTemplate.from_template(
    "You are a helpful coding assistant. Help answer the following question:\n\n{question}"
)

# Chain: prompt -> llm -> output parser
chain: Runnable = prompt | llm | StrOutputParser()

# Streamlit UI
st.set_page_config(page_title="GROQ Coding Assistant", page_icon="🤖")
st.title("🤖 Coding Assistant (GROQ + LangChain)")

question = st.text_area("Ask your coding question:", height=150)

if st.button("Get Answer") and question.strip():
    with st.spinner("Thinking..."):
        try:
            response = chain.invoke({"question": question})
            st.markdown("### 💡 Answer")
            st.code(response, language="python")
        except Exception as e:
            st.error(f"❌ Error: {e}")
