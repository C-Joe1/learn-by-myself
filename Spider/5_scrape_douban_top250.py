import requests
from bs4 import BeautifulSoup

head = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"}
for start_num in range(0, 250, 25):
    response = requests.get(f"https://movie.douban.com/top250?start={start_num}", headers=head)
    if response.ok:
        html = response.text
        soup = BeautifulSoup(html, "html.parser")
        all_titles = soup.find_all("span", attrs={"class": "title"})
        for title in all_titles:
            title_string = title.string
            if '/' not in title_string:
                print(title_string)
    else:
        print(f"\nResponse fail. {response.status_code}")
        break
print("Scrape done.")
