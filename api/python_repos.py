import requests
import plotly.express as px

# Make an API call and check the response.
url = "https://api.github.com/search/repositories"
url += "?q=language:python+sort:stars+stars:>10000"
headers = {"Accept": "application/vnd.github.v3+json"}
r = requests.get(url)
response_json = r.json()
items = response_json["items"]
repo_dict = items[0]
for key in sorted(repo_dict.keys()):
    print(f"{key}: {repo_dict[key]}")
# print(repo_dict)

repo_names, stars = [], []
for repo in items:
    repo_names.append(repo["name"])
    stars.append(repo["stargazers_count"])

fig = px.bar(x=repo_names, y=stars)
fig.show()