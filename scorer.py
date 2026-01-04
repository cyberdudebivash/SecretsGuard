def score_secret(secret_type: str) -> int:
    high_risk = ["AWS Access Key", "GitHub Token"]
    return 90 if secret_type in high_risk else 60
