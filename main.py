import streamlit as st
from langchain_community.chat_models import ChatOllama
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationChain

st.title("AI Chatbot")

if "memory" not in st.session_state:
    st.session_state.memory = ConversationBufferMemory()

if "messages" not in st.session_state:
    st.session_state.messages = []

llm = ChatOllama(model="llama3:8b")
conversation = ConversationChain(llm=llm, memory=st.session_state.memory)

with st.form(key="chat_form", clear_on_submit=True):
    user_input = st.text_input("You:", key="input", placeholder="Ask me anything...")
    submitted = st.form_submit_button("Send")

if submitted and user_input:
    st.session_state.messages.append({"role": "user", "content": user_input})
    response = conversation.run(user_input)
    st.session_state.messages.append({"role": "assistant", "content": response})

for msg in reversed(st.session_state.messages):
    if msg["role"] == "user":
        st.markdown(f"**You:** {msg['content']}")
    else:
        st.markdown(f"**Bot:** {msg['content']}")