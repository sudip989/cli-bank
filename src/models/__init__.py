import uuid
from .accounts import Account
from .transactions import Transaction


def generate_id():
    rparts = str(uuid.uuid4()).split('-')
    return f"{rparts[0]}-{rparts[1]}{rparts[2]}"

__all__ =["Account", "Transaction", "generate_id"]