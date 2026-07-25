import time
from selenium import webdriver
from selenium.webdriver.common.by import By

def test_google_search():
    driver = webdriver.Chrome()
    driver.maximize_window()

    driver.get("https://google.com")

    search_box = driver.find_element(By.NAME, "q")
    search_box.send_keys("Selenium automation testing jobs in Pune")
    search_box.submit()

    time.sleep(3)

    # Assertion: check page title contains keyword
    assert "Selenium" in driver.title

    driver.quit()