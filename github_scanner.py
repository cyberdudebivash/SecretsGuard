from github import Github
from detector import detect_secrets
from scorer import score_secret
from utils import hash_secret, redact
from config import GITHUB_TOKEN
from github.GithubException import GithubException


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
def scan_commit_history(repo_name: str, limit=50):
    """
    PAID FEATURE: Scan commit history for leaked secrets
    """
    gh = Github(GITHUB_TOKEN)
    findings = []

    try:
        repo = gh.get_repo(repo_name)
        commits = repo.get_commits()[:limit]

        for commit in commits:
            if not commit.files:
                continue

            for f in commit.files:
                if not f.patch:
                    continue

                secrets = detect_secrets(f.patch)
                for s in secrets:
                    findings.append({
                        "commit": commit.sha[:7],
                        "file": f.filename,
                        "type": s["type"],
                        "redacted": redact(s["value"]),
                        "hash": hash_secret(s["value"]),
                        "score": score_secret(s["type"]),
                        "source": "commit_history"
                    })

    except GithubException as e:
        findings.append({"error": str(e)})

    return findings

