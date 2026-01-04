from flask import Flask, request, render_template
from github_scanner import scan_repo

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    report = []
    if request.method == "POST":
        repo = request.form["repo"]
        report = scan_repo(repo)
    return render_template("report.html", report=report)

app.run(debug=False)
