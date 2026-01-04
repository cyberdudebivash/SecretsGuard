from detector import detect_secrets
from scorer import score_secret
from utils import hash_secret, redact

def scan_ci_log(text: str):
    results = []
    findings = detect_secrets(text)

    for f in findings:
        results.append({
            "type": f["type"],
            "redacted": redact(f["value"]),
            "hash": hash_secret(f["value"]),
            "score": score_secret(f["type"])
        })
    return results
