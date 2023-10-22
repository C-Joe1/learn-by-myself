from bs4 import BeautifulSoup
import requests

content = requests.get("https://books.toscrape.com/").text
soup = BeautifulSoup(content, "html.parser")

# print(soup.p)
all_prices = soup.find_all("p", attrs={"class": "price_color"})

for price in all_prices:
    print(price.string[2:])

print("\n")
all_title = soup.find_all("h3")
for title in all_title:
    all_links = title.find_all("a") # 此处可用不同方法实现   # link = title.find("a")
    for link in all_links:          # 比如右侧的‘find’方法  # print(link.string)
        print(link.string)          # 可以少一个’for loop‘


# 个人追加任务，将爬到的数据放进定义的字典内
# TODO
