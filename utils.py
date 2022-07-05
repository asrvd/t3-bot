import requests

owner_name = "t3-oss"
repo_name = "create-t3-app"

r = requests.get


def return_issue_or_pr(id: int):
    url = f"https://api.github.com/repos/{owner_name}/{repo_name}/issues/{str(id)}"
    res = requests.get(url)
    if res.status_code == 200:
        data = res.json()
        return data['html_url']
    else:
        return None