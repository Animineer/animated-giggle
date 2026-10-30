import faiss
import numpy as np


# Store our document chunks in memory.
chunks = []


# FAISS needs to know the number of dimensions
# in our embedding vectors.
#
# gemini-embedding-001 currently produces
# 3072-dimensional embeddings.
EMBEDDING_DIMENSION = 3072   #each piece of text is converted into a vector containing 3072 numbers.[0.12, -0.45, 0.78, ..., 0.21]
                            #  1 text - 1 embedding -3072 numbrs

# Create a FAISS index.
#
# IndexFlatL2 performs a straightforward
# similarity search using vector distance.
index = faiss.IndexFlatL2(EMBEDDING_DIMENSION) #like create a container  -index

# Index
#    ↓
# FAISS storage/search structure

# Flat
#    ↓
# Keep the vectors directly

# L2
#    ↓
# Use Euclidean distance


# A = [1, 2]   for 2 dimension
# B = [4, 6]
# The distance is:

# √((4-1)² + (6-2)²)

# = √(9 + 16)

# = √25

# = 5

def add_chunks(new_chunks, embeddings):

    # Remember the actual text.
    chunks.extend(new_chunks)


    # FAISS expects a NumPy array containing
    # floating-point vectors.
    vectors = np.array(
        embeddings,
        dtype="float32"
    )


    # Add the vectors to the FAISS index.
    index.add(vectors)


def search(query_embedding, top_k=3):

    # Convert the query embedding into the format
    # expected by FAISS.
    query_vector = np.array(
        [query_embedding],
        dtype="float32"
    )


    # Search for the closest vectors.
    distances, positions = index.search(
        query_vector,
        top_k
    )


    results = []


    for position in positions[0]:

        # Ignore invalid positions.
        if position == -1:
            continue

        results.append(chunks[position])


    return results