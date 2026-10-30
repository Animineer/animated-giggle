# Change Python request model
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

    # Get the question sent by Node.js.
    question = request.question

    # Send the question to Gemini.
    #
    # model:
    #   The Gemini model we want to use.
    #
    # contents:
    #   The actual user prompt/question.
    response = client.models.generate_content(
        model="gemini-3.8-flash",
        contents=question
    )

    # Return Gemini's generated text to Node.js.
    return {
        "question": question,
        "answer": response.text
    }