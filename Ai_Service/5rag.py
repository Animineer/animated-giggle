from chunking import read_document, create_chunks
from embedding import create_embedding
from vector_store import add_chunks, search


# ---------------------------------------------------------
# STEP 1: Load our document
# ---------------------------------------------------------

file_path = "documents/company.txt"

text = read_document(file_path)


# ---------------------------------------------------------
# STEP 2: Split the document into chunks
# ---------------------------------------------------------

chunks = create_chunks(text)


# ---------------------------------------------------------
# STEP 3: Create an embedding for every chunk
#
# Example:
#
# Chunk 1 → [0.12, -0.03, ...]
# Chunk 2 → [0.41,  0.08, ...]
# ---------------------------------------------------------

embeddings = []

for chunk in chunks:

    vector = create_embedding(chunk)

    embeddings.append(vector)


# ---------------------------------------------------------
# STEP 4: Store chunks + vectors in FAISS
# ---------------------------------------------------------

add_chunks(
    chunks,
    embeddings
)


# ---------------------------------------------------------
# STEP 5: Retrieve relevant chunks
# ---------------------------------------------------------

def retrieve(question, top_k=3):

    # Convert the user's question into an embedding.
    question_embedding = create_embedding(question)


    # Search FAISS for semantically similar chunks.
    results = search(
        question_embedding,
        top_k
    )


    return results