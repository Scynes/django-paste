import uuid

# Generates a short (7 character) randomized id.
def generate():

    result = str(uuid.uuid4())[:8]

    return result

