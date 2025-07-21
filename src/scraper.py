# import necessary modules
from bs4 import BeautifulSoup
from proxy import startProxy, stopProxy
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium_stealth import stealth
import time


PROXIES = {
    'https': 'socks5://127.0.0.1:9050',
    'http': 'socks5://127.0.0.1:9050'
}

chrome_options = Options()
chrome_options.add_argument('--proxy-server=socks5://127.0.0.1:9050')
chrome_options.add_argument("start-maximized")
chrome_options.add_argument("--headless")
chrome_options.add_argument("--window-size=1920,1080")
chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
chrome_options.add_experimental_option('useAutomationExtension', False)
driver = webdriver.Chrome(options=chrome_options)

stealth(driver,
        languages=["en-US", "en"],
        vendor="Google Inc.",
        platform="Win64",
        webgl_vendor="Intel Inc.",
        renderer="Intel Iris OpenGL Engine",
        fix_hairline=True,
        )


def scrape(searches):
    process = startProxy(PROXIES)
    
    text = searches[0]
    url = 'https://www.startpage.com/'
    driver.get(url)
    print('went to page')
    time.sleep(3)

    time.sleep(2)

    search_box = driver.find_element(By.ID, 'q')
    print('found serach box')

    search_box.send_keys(text)
    search_box.send_keys(Keys.RETURN)

    time.sleep(10)  
    driver.quit()