#python test_chunking.py

from chunking import read_document, create_chunks


# Location of our sample document.
file_path = "documents/company.txt"


# Read the document.
text = read_document(file_path)


# Split the document into chunks.
chunks = create_chunks(text)


# Display every chunk.
for i in range(len(chunks)):

    print("\n--------------------")
    print("CHUNK", i + 1)
    print("--------------------")

    print(chunks[i])