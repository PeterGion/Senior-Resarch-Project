'''import imp
from wsgiref import headers
'''
from selenium import webdriver
import time
from bs4 import BeautifulSoup
'''
import requests
requests.utils.default_headers()
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36"}'''
''' latest webdriver version https://chromedriver.chromium.org/home'''
'''page 54 of 55 https://www.indeed.com/jobs?q=software+engineer&l=Connecticut&start=540&pp=gQMqAAABg_wK_jIAAAAB6kOQOQDQAQIBJGAPEZr2bEJzqjuBlPnMPknSJ1Fm60huzKhWMio1Zj5iwgZulLxcHY2NJoB4Zcz6rexHxbPulg-qQXEMry3XEAwpVKu4ucIajpdCNTsWZYvvAdv3R-FR9ZolBHjFezTdCUh2MwEeTE7R31adRPVAxBdlgRll0CpGcNERVBMvB1H2W6mFTFOwUmAGzMrhui_OYTRS_AmSvWqOweZn2WBY02tmlcIlHZBPjYIEBrV8wPqnI7t41NFYVrODDWntyuSfgXwP7CUDxxf5AiTl5QAA&vjk=0e3880292ada0ab1'''
driver = webdriver.Chrome(executable_path="chromedriver")
driver.get("https://www.indeed.com/jobs?q=software+engineer&l=Connecticut&vjk=1d42beca4b168870")
'''Url = driver.current_url
time.sleep(1)
'''
'''page = requests.get(Url)
retry = Retry(connect=5, backoff_factor=0.5, redirect=5)
response = http.request("GET", Url)
response'''
soup = BeautifulSoup(driver.page_source, 'html.parser')
divClass = soup.select_one("div.gnav-header-1dj6m2z > a")
print(divClass.get_text())
'''newTag = divClass.select("a")
print(newTag)'''