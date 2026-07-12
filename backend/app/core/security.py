import secrets
import hashlib


def generate_secret_key(length: int = 32):
    """
    Generate a random secret key.
    """
    return secrets.token_hex(length)


def hash_text(text: str):
    """
    Generate SHA256 hash.
    """
    return hashlib.sha256(text.encode()).hexdigest()
