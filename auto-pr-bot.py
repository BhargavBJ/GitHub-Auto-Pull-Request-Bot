import os
import random
import string
import time
import requests
from git import Repo
from datetime import datetime

GITHUB_USERNAME = "your_github_username"
GITHUB_TOKEN = "your_github_token"
REPO_NAME = "your_repo_name"
TARGET_FILE = "your_target_file.txt"
LOCAL_REPO_PATH = "your_local_repo_path"
DEFAULT_BRANCH = "main"
GITHUB_API_URL = f"https://api.github.com/repos/{GITHUB_USERNAME}/{REPO_NAME}"
NUM_PRS_PER_DAY = random.randint(15, 20)

WORDS = [
    "autonomous", "bot", "generates", "commits", "repository", "pull",
    "request", "GitHub", "automated", "system", "daily", "random",
    "sentence", "python", "script", "workflow", "branch", "feature",
    "test", "integration", "automation", "commit", "push", "version",
    "control", "branching", "merge", "collaboration", "cloud", "ci/cd",
    "deployment", "algorithm", "performance", "debugging", "code", "quality",
    "container", "docker", "dockerfile", "kubernetes", "pipeline", "monitoring",
    "data", "processing", "ai", "machine", "learning", "deep", "neural",
    "network", "training", "model", "optimization", "analytics", "metrics",
    "refactor", "repository", "pull-request", "issue", "feature-branch", "git",
    "merge-conflict", "collaborate", "deploy", "cloud", "api", "endpoint", 
    "server", "networking", "containerization", "orchestration", "load-balancer", 
    "scalability", "database", "sql", "nosql", "storage", "backend", "frontend", 
    "ui", "ux", "react", "angular", "vue", "typescript", "html", "css", "javascript", 
    "responsive", "mobile", "cross-platform", "versioning", "testing", "unit", 
    "integration", "functional", "acceptance", "test-driven", "devops", "agile", 
    "scrum", "project", "management", "documentation", "sprint", "iteration", "backlog", 
    "feature-request", "bug-fix", "release", "hotfix", "patch", "upgrade", "rollback",
    "monitoring", "logging", "error-handling", "validation", "security", "authentication",
    "authorization", "access", "control", "permissions", "encryption", "data-protection"
]


def generate_random_sentence():
    length = random.randint(5, 10)
    words = random.choices(WORDS, k=length)
    return ' '.join(words).capitalize() + '.\n'

def append_sentence_to_file(file_path):
    with open(file_path, 'a') as f:
        f.write(generate_random_sentence())

def random_branch_name():
    return 'branch-' + ''.join(random.choices(string.ascii_lowercase + string.digits, k=8))

def create_pull_request(branch_name):
    headers = {
        "Authorization": f"token {GITHUB_TOKEN}",
        "Accept": "application/vnd.github+json"
    }

    data = {
        "title": f"Auto PR - {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}",
        "head": branch_name,
        "base": DEFAULT_BRANCH,
        "body": "This PR was generated automatically by the bot. It contains a random sentence."
    }

    response = requests.post(f"{GITHUB_API_URL}/pulls", headers=headers, json=data)

    if response.status_code == 201:
        print(f"[+] Pull request created: {response.json()['html_url']}")
    else:
        print(f"[!] PR creation failed: {response.status_code} - {response.text}")

def main():
    repo = Repo(LOCAL_REPO_PATH)
    origin = repo.remote(name='origin')
    file_path = os.path.join(LOCAL_REPO_PATH, TARGET_FILE)

    for i in range(NUM_PRS_PER_DAY):
        print(f"\nCreating PR {i+1}/{NUM_PRS_PER_DAY}...")

        repo.git.checkout(DEFAULT_BRANCH)
        repo.git.pull()
        branch_name = random_branch_name()
        repo.git.checkout('-b', branch_name)

        append_sentence_to_file(file_path)

        repo.git.add(A=True)
        repo.index.commit(f"Add random sentence {i+1}")
        origin.push(branch_name)

        create_pull_request(branch_name)

        sleep_time = random.randint(30, 90)
        print(f"Sleeping {sleep_time}s before next PR...")
        time.sleep(sleep_time)

if __name__ == "__main__":
    main()
