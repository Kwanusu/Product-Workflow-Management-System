import requests

base_Url = 'https://jsonplaceholder.typicode.com/users'
search_terms = {
    'userId': 1,
    'completed': 'false'
}

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36...",
    "Accept": "application/json"
}

response = requests.get(base_Url, params=search_terms, headers=headers)

data = response.json()

print(response.url)