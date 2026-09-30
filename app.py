import os
import streamlit as st
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

st.set_page_config(page_title="ShopAI", page_icon="🛍️")
st.title("🛍️ ShopAI")
st.caption("Atendimento inteligente da nossa loja online")

if "messages" not in st.session_state:
    st.session_state["messages"] = [
        {
            "role": "system",
            "content": "Você é o ShopAI, assistente de uma loja online. Ajude os clientes com produtos, pedidos, dúvidas e recomendações."
        }
    ]

for message in st.session_state["messages"]:
    if message["role"] != "system":
        with st.chat_message(message["role"]):
            st.write(message["content"])

if prompt := st.chat_input("Como posso ajudar?"):
    st.session_state["messages"].append(
        {"role": "user", "content": prompt}
    )

    with st.chat_message("user"):
        st.write(prompt)

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=st.session_state["messages"]
    )

    answer = response.choices[0].message.content

    st.session_state["messages"].append(
        {"role": "assistant", "content": answer}
    )

    with st.chat_message("assistant"):
        st.write(answer)