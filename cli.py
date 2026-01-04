import sys
from github_scanner import scan_repo
from rich import print

if len(sys.argv) != 2:
    print("[red]Usage:[/red] python cli.py owner/repo")
    sys.exit(1)

repo = sys.argv[1]
results = scan_repo(repo)

print(f"[bold]SecretsGuard Report for {repo}[/bold]")

for r in results:
    print(r)
