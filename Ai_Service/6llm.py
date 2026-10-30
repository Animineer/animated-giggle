from google import genai
from dotenv import load_dotenv
import os


# Load the API key from .env.
load_dotenv()


api_key = os.getenv("GEMINI_API_KEY")


# Create the Gemini client.
client = genai.Client(
    api_key=api_key
)


def generate_answer(question, context):

    # Give Gemini the retrieved information.
    #
    # The model should answer using this context
    # instead of relying only on its general knowledge.
    prompt = """
You are a helpful technical assistant.

Answer the user's question using the provided context.

Rules:
- Use the context when it contains the answer.
- Do not invent information.
- If the context does not contain enough information,
  clearly say that the information is not available.

Context:
""" + context + """

User question:
""" + question


    # Ask Gemini to generate the final answer.
    response = client.models.generate_content(
        model="gemini-3.8-flash",
        contents=prompt
    )


    return response.text