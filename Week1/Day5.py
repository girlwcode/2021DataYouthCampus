"""
DAY5 : Crawling 실습
"""
from selenium import webdriver

driver_path = '../resources/chromedriver.exe'
# url = "https://play.google.com/store/apps/top/category/GAME"
urls = [
    "https://play.google.com/store/apps/top/category/GAME_EDUCATIONAL",
    "https://play.google.com/store/apps/top/category/GAME_WORD"
]
browser = webdriver.Chrome(executable_path=driver_path)

for url in urls :
    browser.get(url)

browser.quit()