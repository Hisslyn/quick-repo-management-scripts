import requests

# Replace these with your actual details
USERNAME = "your username"
TOKEN = "your token"

# GitHub API URL
API_URL = "https://api.github.com/user/repos"

headers = {
    "Authorization": f"token {TOKEN}"
}

# Fetch all repositories
response = requests.get(API_URL, headers=headers)
repos = response.json()

for repo in repos:
    if not repo["archived"]:  # Check if the repository is already archived
        repo_name = repo["name"]
        repo_url = repo["url"]
        print(f"Archiving {repo_name}...")
        # Update repository to archived
        update_response = requests.patch(
            repo_url,
            json={"archived": True},
            headers=headers
        )
        if update_response.status_code == 200:
            print(f"{repo_name} is now archived.")
        else:
            print(f"Failed to archive {repo_name}: {update_response.status_code}")
