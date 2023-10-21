import requests

head = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"}
response = requests.get("https://movie.douban.com/top250", headers=head)

if response.ok:
    print(response.text)
    print(f"\nResponse done. {response.status_code}")
else:
    print(f"\nResponse fail. {response.status_code}")
