import requests

# Vars needed for the API
GITHUB_TOKEN = input("Paste your generated github token : ")
GITHUB_USERNAME = input("Write your username : ")
REPO_NAME = "versioning_exam"  # Name for the new repository
REPO_DESCRIPTION = "Created from script"  # Description for the new repository
ISSUE_TITLES = ["First big issue", "Second little issue"]
ISSUE_BODIES = [
    "Really critical issue i need help",
    "Little bug discorved. Here's the replication steps",
]  # Descriptions for the issues

# Auth headers
headers = {
    "Authorization": f"token {GITHUB_TOKEN}",
    "Accept": "application/vnd.github.v3+json",
}


# Function to create a new repo
def create_repository():
    url = "https://api.github.com/user/repos"
    payload = {
        "name": REPO_NAME,
        "description": REPO_DESCRIPTION,
        "private": False,  # Public repository
    }

    response = requests.post(url, json=payload, headers=headers)

    if response.status_code == 201:
        print(f"Repository '{REPO_NAME}' created successfully.")
        return response.json()  # Returns the repository details as a dictionary
    else:
        print(f"Repository creation failed: {response.status_code}")
        print(response.json())
        return None


# Step 2: Create issues in the new repository
def create_issues(repo_full_name):
    for title, body in zip(ISSUE_TITLES, ISSUE_BODIES):
        url = f"https://api.github.com/repos/{repo_full_name}/issues"
        payload = {"title": title, "body": body}

        response = requests.post(url, json=payload, headers=headers)

        if response.status_code == 201:
            print(f"Issue '{title}' created successfully.")
        else:
            print(f"Failed to create issue '{title}': {response.status_code}")
            print(response.json())


# Main Execution
if __name__ == "__main__":
    repo_details = create_repository()
    if repo_details:
        create_issues(
            repo_details["full_name"]
        )  # Get full name from creation http answer
