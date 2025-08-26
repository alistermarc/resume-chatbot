import gradio as gr
from chatbot import Chatbot

if __name__ == "__main__":
    chatbot = Chatbot()
    with gr.Blocks(theme=gr.themes.Citrus(), title="My Resume Chatbot") as demo:
        gr.Markdown("""
        # Alister's Resume Chatbot
        Ask me anything about my resume, skills, and experience.
        """)
        gr.ChatInterface(chatbot.chat, type="messages")
    demo.launch()