# import necessary modules
from bs4 import BeautifulSoup
from proxy import startProxy, stopProxy
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
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
service = Service(executable_path='./chromedriver.exe')


def scrape(searches):
    driver = webdriver.Chrome(options=chrome_options, service=service)

    stealth(driver,
            languages=["en-US", "en"],
            vendor="Google Inc.",
            platform="Win64",
            webgl_vendor="Intel Inc.",
            renderer="Intel Iris OpenGL Engine",
            fix_hairline=True,
            )
    
    process = startProxy(PROXIES)
    
    url = 'https://www.startpage.com/'
    driver.get(url)

    time.sleep(4)

    links = {}

    for search in searches:
        hrefs = []
        print(search)
        search_box = driver.find_element(By.ID, 'q')
        search_box.send_keys(Keys.CONTROL + 'a')
        search_box.send_keys(Keys.DELETE)
        search_box.send_keys(search)
        search_box.send_keys(Keys.RETURN)
        page = driver.page_source

        time.sleep(3)

        soup = BeautifulSoup(page, 'html.parser')
        a_elements = soup.find_all('a', class_='result-title result-link css-1ubyvt6')
        for a in a_elements:
            hrefs.append(a.get('href'))
        
        links[search] = hrefs
        
        time.sleep(3)
    

    time.sleep(5)
    process.kill()
    driver.quit()
    print(links)
    return links