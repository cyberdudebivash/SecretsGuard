from github import Github
from detector import detect_secrets
from scorer import score_secret
from utils import hash_secret, redact
from config import GITHUB_TOKEN

def scan_repo(repo_name: str):
    gh = Github(GITHUB_TOKEN)
    repo = gh.get_repo(repo_name)

    results = []

    for file in repo.get_contents(""):
        if file.type != "file":
            continue

        content = file.decoded_content.decode(errors="ignore")
        findings = detect_secrets(content)

        for f in findings:
            results.append({
                "file": file.path,
                "type": f["type"],
                "redacted": redact(f["value"]),
                "hash": hash_secret(f["value"]),
                "score": score_secret(f["type"])
            })

    return results
