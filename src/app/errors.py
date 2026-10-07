class InvalidAmount(Exception):
    """Raise this exception when the amount is invalid or negative"""
    
    pass

class AccountNotFound(Exception):
    """Raise this exception when account id does not exists."""
    pass