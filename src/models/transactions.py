from typing import Literal
import datetime
from src.models import generate_id



class Transaction:
    def __init__(self, txn_type: Literal["deposit", "withdraw","transfer"], amount: float, source_id: str, target_id: str):
        self._id = generate_id()
        self.txn_type = txn_type
        self.amount = amount
        self.source_id = source_id
        self.target_id = target_id
        self.timestamp = datetime.datetime.now().isoformat()