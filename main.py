from selenium import webdriver
import time
from bs4 import BeautifulSoup

# chrome driver option參數
# 可參考https://www.itread01.com/content/1544787185.html
options = webdriver.ChromeOptions()
# 不加載圖片
options.add_argument('blink-settings=imagesEnabled=false')

# chrome driver放在專案目錄下，如果不是放在專案目錄下，則需另外指定路徑
# driver = webdriver.Chrome(executable_path="chrome driver路徑")
driver = webdriver.Chrome(options=options)
driver.get("該用戶的喜歡url")

# 使用JS下拉網頁，每拉一次等兩秒
SCROLL_PAUSE_TIME = 2

last_height = driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
while True:
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(SCROLL_PAUSE_TIME)
    new_height = driver.execute_script("return document.body.scrollHeight")
    if new_height == last_height:
        break
    last_height = new_height

# 找出所有連結
# Beautiful Soup 解析 HTML 程式碼
html = driver.page_source
soup = BeautifulSoup(html, "lxml")
# 使用css selecter取得a tag
all_links = soup.select('div.isayt>a')

# 將連結寫入txt檔
f = open('./all_links2.txt','w')
for link in all_links:
    f.write(link.get('href'))
    f.write('\n')
f.close()

driver.close()