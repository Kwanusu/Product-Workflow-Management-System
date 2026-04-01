import requests
import time
base_Url = 'https://jsonplaceholder.typicode.com/posts'

for i in range(5):
    requests.get(base_Url)
    print(f"Fetched page {i}")
    time.sleep(1)
