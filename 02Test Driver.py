from selenium import webdriver

def main():
    driver = webdriver.Chrome()
    driver.get("https://www.baidu.com")

if __name__ == '__main__':
    main()