import streamlit as st

from app.chatbot import CorporateAIAgent


st.set_page_config(
    page_title="Asistente de Devoluciones",
    page_icon="🤖",
    layout="wide"
)


st.title("🤖 Asistente de Devoluciones")

st.write(
    "¡Hola! 👋 Estoy aquí para ayudarte con tus dudas sobre "
    "las políticas de devolución."
)


if "agent" not in st.session_state:
    with st.spinner("Casi listo... estoy preparando el asistente."):
        agent = CorporateAIAgent()
        agent.initialize()
        st.session_state.agent = agent


question = st.text_input(
    "Escribe aquí tu duda sobre devoluciones:",
    placeholder="Ejemplo: ¿Cuánto tiempo tengo para devolver un producto?"
)


if st.button("Consultar"):
    if question.strip():
        with st.spinner("Estoy revisando la información para ti..."):
            answer = st.session_state.agent.ask(question)

        st.success(answer)

    else:
        st.warning("Cuéntame primero qué quieres saber 😊")