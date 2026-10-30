from rag import retrieve
from llm import generate_answer


# The question we want to ask.
question = "How does Part Allocation work?"


# ---------------------------------------------------------
# RETRIEVAL
#
# Find the document chunks that are most relevant
# to the user's question.
# ---------------------------------------------------------

relevant_chunks = retrieve(
    question,
    top_k=3
)


print("\nRetrieved chunks:\n")


for chunk in relevant_chunks:

    print("--------------------")

    print(chunk)


# ---------------------------------------------------------
# CONTEXT
#
# Combine the retrieved chunks into one context
# for Gemini.
# ---------------------------------------------------------

context = "\n\n".join(
    relevant_chunks
)


# ---------------------------------------------------------
# GENERATION
#
# Give the retrieved context + question to Gemini.
# ---------------------------------------------------------

answer = generate_answer(
    question,
    context
)


print("\n\nAI ANSWER:")
print(answer)