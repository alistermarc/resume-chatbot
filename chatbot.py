from openai import OpenAI
import json
from pypdf import PdfReader
from tools import tools, record_user_details, record_unknown_question
from config import GROQ_API_KEY

class Chatbot:

    def __init__(self):
        self.client = OpenAI(
            base_url="https://api.groq.com/openai/v1",
            api_key=GROQ_API_KEY
        )
        self.name = "Alister Marc Domilies"
        reader = PdfReader("me/resume.pdf")
        self.linkedin = ""
        for page in reader.pages:
            text = page.extract_text()
            if text:
                self.linkedin += text
        with open("me/summary.txt", "r", encoding="utf-8") as f:
            self.summary = f.read()


    def handle_tool_call(self, tool_calls):
        results = []
        for tool_call in tool_calls:
            tool_name = tool_call.function.name
            arguments = json.loads(tool_call.function.arguments)
            print(f"Tool called: {tool_name}", flush=True)
            tool = globals().get(tool_name)
            result = tool(**arguments) if tool else {}
            results.append({"role": "tool","content": json.dumps(result),"tool_call_id": tool_call.id})
        return results
    
    def system_prompt(self):
        return f"""You are acting as {self.name}. You are answering questions on {self.name}'s website, 
    particularly questions related to {self.name}'s career, background, skills and experience. 
    Your responsibility is to represent {self.name} for interactions on the website as faithfully as possible. 
    You are given a summary of {self.name}'s background and LinkedIn profile which you can use to answer questions. 
    Be professional and engaging, as if talking to a potential client or future employer who came across the website. 
    If you don't know the answer to any question, use your record_unknown_question tool to record the question that you couldn't answer, even if it's about something trivial or unrelated to career. 
    If the user is engaging in discussion, try to steer them towards getting in touch via email; ask for their email and record it using your record_user_details tool. 

    ## Summary:
    {self.summary}

    ## LinkedIn Profile:
    {self.linkedin}

    With this context, please chat with the user, always staying in character as {self.name}."""
    
    def chat(self, message, history):
        cleaned_history = []
        for item in history:
            cleaned_history.append({"role": item['role'], "content": item['content']})

        messages = [{"role": "system", "content": self.system_prompt()}] + cleaned_history + [{"role": "user", "content": message}]
        
        response = self.client.chat.completions.create(model="llama-3.1-8b-instant", messages=messages, tools=tools)
        response_message = response.choices[0].message

        if response_message.tool_calls:
            results = self.handle_tool_call(response_message.tool_calls)
            messages.append(response_message)
            messages.extend(results)
            
            # Second call to get the final response
            response = self.client.chat.completions.create(model="openai/gpt-oss-20b", messages=messages, tools=tools)
            return response.choices[0].message.content

        return response_message.content