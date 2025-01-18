import io

import ddddocr
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from PIL import Image


# 创建一个浏览器对象，这里使用 Chrome 浏览器，需要提前安装好 Chrome 浏览器和对应的 ChromeDriver
driver = webdriver.Chrome()
driver.maximize_window()

time.sleep(2)
# 打开网页
driver.get('https://sfgl.njtech.edu.cn/cas/login')  # 将 'https://example.com' 替换为你需要登录的实际网址

time.sleep(5)

# <img _ngcontent-bej-c294="" class="code-img" src="/cas/api/captcha/generate/DEFAULT">
code_img = driver.find_element(By.CLASS_NAME, 'code-img')

location = code_img.location
size = code_img.size

# 保存整个页面截图
driver.save_screenshot('full_page_screenshot.png')
# 打开截图
image = Image.open('full_page_screenshot.png')

print(location)
print(size)
# 截取验证码区域
addx=715
addy=190
captcha_image = image.crop(
    (location['x']+addx, location['y']+addy, location['x'] +addx+ size['width']+45, location['y'] +addy+ size['height']+10))

# 保存验证码图片
captcha_image.save('captcha.png')


ocr = ddddocr.DdddOcr()
with open('captcha.png', 'rb') as f:
    img_bytes = f.read()
    res = ocr.classification(img_bytes)

print(res)
driver.close()