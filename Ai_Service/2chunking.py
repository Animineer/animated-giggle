# Read the complete document.
def read_document(file_path):
    
     # Open the file in read mode using UTF-8 encoding.
    with open(file_path, "r", encoding="utf-8") as file:

        text = file.read()

    return text


# Split the document into smaller pieces.
#
# chunk_size:
#     Maximum number of characters in each chunk.
#
# overlap:  (preserve -my name is pankaj- your name is pankaj - give data in flow)
#     Number of characters repeated between
#     consecutive chunks.
def create_chunks(text, chunk_size=300, overlap=50):

    chunks = []

    start = 0

    while start < len(text):

        # Calculate where this chunk should end.
        end = start + chunk_size

        # Extract the current chunk.
        chunk = text[start:end]

        chunks.append(chunk)

        # Move forward.
        #
        # We subtract overlap so that some information
        # from the previous chunk is retained.
        start = end - overlap

    return chunks