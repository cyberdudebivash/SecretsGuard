import sys
from rich import print
from github_scanner import scan_repo, scan_commit_history

if len(sys.argv) < 2:
    print("[red]Usage:[/red] python cli.py owner/repo [--history]")
    sys.exit(1)

repo = sys.argv[1]
scan_history = "--history" in sys.argv

print(f"[bold]SecretsGuard Report for {repo}[/bold]")

results = scan_repo(repo)

if scan_history:
    print("[yellow]⚠ Commit history scanning enabled (PRO feature)[/yellow]")
    history_results = scan_commit_history(repo)
    results.extend(history_results)

if not results:
    print("[green]✔ No secrets detected. Repository appears clean.[/green]")
    sys.exit(0)

for r in results:
    if "error" in r:
        print(f"[red]{r['error']}[/red]")
    else:
        print(r)
