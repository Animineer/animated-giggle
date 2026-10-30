from fastapi import FastAPI

# Create the FastAPI application.
# This "app" object will receive HTTP requests.
app = FastAPI()


# GET /ai/hello
#
# This is our first AI-service endpoint.
# We are NOT calling an LLM yet.
# First we make sure Node can communicate with Python.
@app.get("/ai/hello")
def hello_ai():

    return {
        "message": "Hello from AI service"
    }