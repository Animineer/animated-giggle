#Build Gemini context

from fastapi import FastAPI
from pydantic import BaseModel
from google import genai
from dotenv import load_dotenv
import os


# Load variables from the .env file.
#
# This allows us to keep the Gemini API key
# outside the source code.
load_dotenv()


# Read the Gemini API key from the environment.
api_key = os.getenv("GEMINI_API_KEY")


# Create the Gemini client.
#
# The client is responsible for communicating
# with Google's Gemini API.
client = genai.Client(api_key=api_key)


# Create the FastAPI application.
app = FastAPI()


# This describes the JSON request that our API expects.
#
# Example:
# {
#     "question": "What is REST API?"
# }
class AIMessage(BaseModel):

    # "user" or "assistant"
    role: str

    # Actual message text.
    content: str


class AIRequest(BaseModel):

    # New question from the user.
    question: str

    # Previous conversation messages.
    messages: list[AIMessage] = []

# AI endpoint
#
# Node.js will call this endpoint.
@app.post("/ai/ask")
def ask_ai(request: AIRequest):

    # This list will contain the previous conversation
    # plus the user's new question.
    conversation = []


    # Add previous messages.
    for message in request.messages:

        conversation.append(
            message.role + ": " + message.content
        )


    # Add the latest question.
    conversation.append(
        "user: " + request.question
    )


    # Convert the conversation into one prompt.
    prompt = "\n".join(conversation)


    # Send the complete context to Gemini.
    response = client.models.generate_content(
        model="gemini-3.8-flash",
        contents=prompt
    )


    return {
        "answer": response.text
    }