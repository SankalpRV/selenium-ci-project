import time
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

def test_google_search():
    chrome_options = Options()
    chrome_options.add_argument("--headless=new")
    chrome_options.add_argument("--start-maximized")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--no-sandbox")

    driver = webdriver.Chrome(options=chrome_options)

    base_url = os.getenv("BASE_URL")
    driver.get(base_url)

    search_box = driver.find_element(By.NAME, "q")
    search_box.send_keys("Selenium automation testing jobs in Pune")
    search_box.submit()

    time.sleep(2)

    assert "Selenium" in driver.title

    driver.quit()