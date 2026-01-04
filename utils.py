import hashlib

def hash_secret(secret: str) -> str:
    return hashlib.sha256(secret.encode()).hexdigest()

def redact(secret: str) -> str:
    if len(secret) < 6:
        return "***"
    return secret[:2] + "***" + secret[-2:]
