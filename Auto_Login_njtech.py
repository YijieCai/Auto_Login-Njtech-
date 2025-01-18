import ddddocr
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from PIL import Image
import subprocess


def restart_computer():
    subprocess.run(["shutdown", "/r", "/t", "0"])

def is_online():
    try:
        response = requests.get("https://www.baidu.com", timeout=5)
        return response.status_code == 200
    except requests.exceptions.ConnectionError:
        return False

Login_try_number=0
while 1:
    if is_online():
        # is online
        print('有网，一小时后重试')
        Login_try_number=0
        time.sleep(3600)
        continue
    else:
        # is offline
        Login_try_number = Login_try_number + 1
        try:
            driver = webdriver.Chrome()
            driver.maximize_window()
            time.sleep(10)
            # 打开网页
            driver.get('https://sfgl.njtech.edu.cn/cas/login')  # 将 'https://example.com' 替换为你需要登录的实际网址
            time.sleep(10)

            #get code image
            code_img = driver.find_element(By.CLASS_NAME, 'code-img')
            location = code_img.location
            size = code_img.size
            driver.save_screenshot('full_page_screenshot.png')
            image = Image.open('full_page_screenshot.png')
            addx = 715
            addy = 190
            captcha_image = image.crop(
                (location['x'] + addx, location['y'] + addy, location['x'] + addx + size['width'] + 45,
                 location['y'] + addy + size['height'] + 10))
            captcha_image.save('captcha.png')


            # OCR code
            ocr = ddddocr.DdddOcr()
            with open('captcha.png', 'rb') as f:
                img_bytes = f.read()
                res = ocr.classification(img_bytes)


            # input
            username_input = driver.find_element(By.NAME, "username")
            username_input.send_keys('202462126309')

            password_input = driver.find_element(By.XPATH,
                                                 '//*[@id="login-normal"]/div[2]/form/div[2]/nz-input-group/input')
            password_input.send_keys('Caiyijie123@@')  # 将 'your_password' 替换为你的实际密码

            code_input = driver.find_element(By.XPATH,
                                             '//*[@id="login-normal"]/div[2]/form/app-verification/nz-input-group/input')
            code_input.send_keys(res)

            #click
            login_button = driver.find_element(By.XPATH, '//*[@id="login-normal"]/div[2]/form/div[6]')
            login_button.click()

            time.sleep(10)
            driver.close()
        except:
            time.sleep(30)
        if Login_try_number >1200:
            restart_computer()
    # print(Login_try_number)