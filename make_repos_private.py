import requests

# Replace with your GitHub username and personal access token
USERNAME = "your username"
TOKEN = "your token"

# API URL
API_URL = "https://api.github.com/user/repos"

headers = {
    "Authorization": f"token {TOKEN}"
}

# Get all repositories
response = requests.get(API_URL, headers=headers)
repos = response.json()

for repo in repos:
    if not repo["private"]:
        repo_name = repo["name"]
        repo_url = repo["url"]
        print(f"Making {repo_name} private...")
        # Update repository to private
        update_response = requests.patch(
            repo_url,
            json={"private": True},
            headers=headers
        )
        if update_response.status_code == 200:
            print(f"{repo_name} is now private.")
        else:
            print(f"Failed to update {repo_name}: {update_response.status_code}")
