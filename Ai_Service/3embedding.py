from google import genai
from dotenv import load_dotenv
import os


# Load values from .env.
load_dotenv()


# Read the Gemini API key.
api_key = os.getenv("GEMINI_API_KEY")


# Create the Google AI client.
client = genai.Client(api_key=api_key)


# Convert text into an embedding vector.
def create_embedding(text):

    response = client.models.embed_content(

        # Embedding model.
        model="gemini-embedding-001",

        # Text that we want to convert into numbers.
        contents=text
    )

    # Return the generated vector.
    return response.embeddings[0].values