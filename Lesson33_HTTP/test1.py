import requests

response = requests.get(
    "https://api.github.com/search/repositories",
    params={"q": '"real python"'},
    headers={"Accept": "application/vnd.github.text-match+json"},
)

json_response = response.json()
first_repository = json_response["items"][0]
print(first_repository["text_matches"][0]["matches"])