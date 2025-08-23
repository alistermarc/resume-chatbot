# Alister's Resume Chatbot

This is a chatbot that can answer questions about my resume, skills, and experience.

## Description

This project is a resume chatbot that acts as myself, answering questions about his career, background, skills, and experience. It uses a Gradio interface for the chat and the OpenAI LLM for the chatbot's intelligence. The chatbot is provided with a resume in PDF format and a text summary to answer questions accurately. It also has the ability to record user details (name, email, notes) and any questions it cannot answer.

## Getting Started

### Installation

1. Clone the repo
   ```sh
   git clone https://github.com/your_username/resume-chatbot.git
   ```
2. Install PIP packages
   ```sh
   pip install -r requirements.txt
   ```
3. Create a `.env` file in the root directory and add the following variables:
   ```
   PUSHOVER_TOKEN=your_pushover_token
   PUSHOVER_USER=your_pushover_user
   OPENAI_API_KEY=your_openai_api_key
   ```

## Usage

Run the application using the following command:
```sh
python app.py
```
This will launch a Gradio interface in your browser. You can then ask questions about my resume.

## Deployment

You can access the chatbot on Hugging Face Spaces:
[https://huggingface.co/spaces/alistermarc/resume_chatbot](https://huggingface.co/spaces/alistermarc/resume_chatbot)
