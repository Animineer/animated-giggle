 # Instructions that define how the AI should behave.
 #Prompt Engineering + Context Management.
@app.post("/ai/ask")
def ask_ai(request: AIRequest):

    # Instructions that define how the AI should behave.
    system_instruction = """
You are a helpful technical assistant.

Rules:
- Explain technical concepts clearly.
- Prefer practical examples.
- Use previous conversation when answering follow-up questions.
- If you do not know something, say so.
"""


    # Build the conversation context.
    conversation = []

    for message in request.messages:

        conversation.append(
            message.role + ": " + message.content
        )


    # Add the current user question.
    conversation.append(
        "user: " + request.question
    )


    # Combine instructions and conversation.
    prompt = (
        system_instruction
        + "\n\nConversation:\n" # add readable seperter
        + "\n".join(conversation)  # combine all convrsation
    )


    # Send the final prompt to Gemini.
    response = client.models.generate_content(
        model="gemini-3.8-flash",
        contents=prompt
    )


    return {
        "answer": response.text
    }