import re

SECRET_PATTERNS = {
    "AWS Access Key": r"AKIA[0-9A-Z]{16}",
    "GitHub Token": r"ghp_[A-Za-z0-9]{36}",
    "Generic API Key": r"(?i)api[_-]?key['\"]?\s*[:=]\s*['\"][A-Za-z0-9]{16,}['\"]"
}

def detect_secrets(text: str):
    findings = []
    for name, pattern in SECRET_PATTERNS.items():
        for match in re.findall(pattern, text):
            findings.append({
                "type": name,
                "value": match
            })
    return findings
