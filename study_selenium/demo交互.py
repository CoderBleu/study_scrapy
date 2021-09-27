from selenium import webdriver
import  time

# 创建浏览器操作对象
path = 'file/chromedriver.exe'

browser = webdriver.Chrome(path)

url = 'https://www.baidu.com'
browser.get(url)

# 休眠2秒
time.sleep(2)

# 获取文本框的对象
input = browser.find_element_by_id('kw')

# 在文本框总输入周杰伦
input.send_keys('周杰伦')

time.sleep(2)

# 获取百度一下的按钮
button = browser.find_element_by_id('su')

# 点击按钮
button.click()

time.sleep(2)

# 滑倒底部
js_scroll_to_footer = 'document.documentElement.scrollTop=10000'
browser.execute_script(js_scroll_to_footer)

time.sleep(2)

# 获取下一页的按钮
next = browser.find_element_by_xpath('//a[@class="n"]')

# 点击下一页
next.click()

time.sleep(2)

# 回到上一页
browser.back()

# 回去
browser.forward()

time.sleep(3)