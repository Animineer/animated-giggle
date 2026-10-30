from embedding import create_embedding


text = """
Part Allocation is used to allocate finished goods
to production-related child parts.
"""


# Convert the text into a vector.
vector = create_embedding(text)


print("Number of dimensions:", len(vector))

print("\nFirst 10 values:")

for i in range(10):

    print(vector[i])