# 导入 requests 库
import requests

# 定义字典 head，储存用于伪装的 User-Agent 键值对
head = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"}

# 定义 response 变量，通过 get 方法获取 URL 所对应的服务器所返回的 text文本
# 同时通过 headers 参数，传入 head 字典
# 这样在向服务器发起请求时，爬虫就会伪装成字典中对应的 User-Agent 数据
response = requests.get("https://books.toscrape.com/", headers=head)

# 条件判定，通过 ok 方法与 status_code 方法判断请求是否成功。
if response.ok:
    print(response.text)
    print(f"\nResponse done. {response.status_code}")
else:
    print(f"\nResponse fail. {response.status_code}")
