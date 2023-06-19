import os
from github import Github

token = os.getenv("GH_TOKEN")
repo_name = os.getenv("PULL_REQUEST_REPO")  # org/repo format
repo_number = os.getenv("PULL_REQUEST_NUMBER")

print ("token--", token)
print ("repo_name--", repo_name)
print ("repo_number--", repo_number)

g = Github(token)
repo = g.get_repo(repo_name)
pull_request = repo.get_pull(int(os.getenv("PULL_REQUEST_NUMBER")))

print ("repo", repo)
print ("pull_request", pull_request)
