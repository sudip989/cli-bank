import uuid

def generate_id():
    rparts = str(uuid.uuid4()).split('-')
    return f"{rparts[0]}-{rparts[1]}{rparts[2]}"

print(generate_id())