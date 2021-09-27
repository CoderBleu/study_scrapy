'''
handless无界面的驱动浏览器
'''

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')

# path是你自己的chrome浏览器的文件路径
path = r'C:\Program Files (x86)\Google\Chrome\Application\chrome.exe'
chrome_options.binary_location = path

# 注意chromedriver.exe路径
browser = webdriver.Chrome(executable_path='file/chromedriver.exe',chrome_options=chrome_options)

url = 'https://www.baidu.com'
browser.get(url)

browser.save_screenshot('baidu.png')