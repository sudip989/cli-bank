import os
import json

from src.config import DB_DIR, ACC_JSON, TXN_JSON
from src.models import Account, Transaction


def ensure_files():
    """Ensure all the file and folders exists when the code runs."""

    os.makedirs(DB_DIR,exist_ok=True)
    for i in (ACC_JSON, TXN_JSON):
        with open(f"{DB_DIR}/{i}", "w") as f:
            json.dump([], f, indent=4)

def save_accounts(accounts: list[Account]):
    """Save all accounts details to it's relevant json file."""
    with open(ACC_JSON, "w") as f:
        json.dump([acc.to_dict() for acc in accounts], f, indent=4)


def save_transaction(txn: Transaction):
    """Save a tranasaction details to it's relevant jason file"""
    with open(TXN_JSON, "r") as f:
        data = list(json.load(f))

    data.append(txn.to_dict())

    with open(TXN_JSON, "w") as f:
        json.dump(data, f, indent=4)

def load_accounts() -> list[Account]:
    """Load all account details from the relevant json file"""
    
    with open(ACC_JSON, "r") as f:
        result = list(json.load(f))

    return [Account.from_dict(acc) for acc in result]
