from fastapi import FastAPI
from pydantic import BaseModel

# Create the FastAPI application.
app = FastAPI()


# This class describes the JSON data that our API expects.
#
# Example request:
# {
#     "question": "What is REST API?"
# }
#
# Pydantic validates the incoming data for us.
class AIRequest(BaseModel):

    question: str


# AI endpoint
#
# Node will call this endpoint and send the user's question.
@app.post("/ai/ask")
def ask_ai(request: AIRequest):

    # Access the question sent by Node.
    question = request.question

    # For now we are NOT calling Gemini.
    # We are simply proving that Python received the question.
    return {
        "question_received": question,
        "answer": "Python received your question successfully."
    }