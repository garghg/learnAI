# import necessary modules
from bs4 import BeautifulSoup
from proxy import startProxy, stopProxy
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import time


PROXIES = {
    'http': 'socks5://127.0.0.1:9050',
    'https': 'socks5://127.0.0.1:9050'
}


chrome_options = Options()
chrome_options.add_argument('--proxy-server=socks5://127.0.0.1:9050')
# chrome_options.add_argument("--headless")
service = Service(executable_path="./chromedriver.exe")
driver = webdriver.Chrome(service=service, options=chrome_options)


def scrape(searches):
    try:
        process = startProxy(PROXIES)
    except:
        stopProxy(process)
        process = startProxy(PROXIES)
    text = searches[0]
    url = 'https://youtube.com/'
    page = driver.get(url)
    time.sleep(2)
    search_box = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.NAME, 'search_query'))
    )
    search_box.clear()
    search_box.send_keys(text)
    search_box.send_keys(Keys.RETURN)
    soup = BeautifulSoup(page.text, "html.parser")
    link = soup.find_all('a')
    print(link)
    time.sleep(10)  
    driver.close()
