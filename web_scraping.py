import requests
from bs4 import BeautifulSoup
# ライブラリのインポート

# URLの指定。ページ情報の取得
r = requests.get('https://news.yahoo.co.jp')

print(r.headers)
print(r.status_code)

soup = BeautifulSoup(r.content, "html.parser")

# "主要"ニュースのタイトルを取ってくる 
print(soup.find("div",id="tpc_maj").find_all("a").prettify())
