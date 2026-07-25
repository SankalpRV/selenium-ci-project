import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.maximize_window()

# 1. Open Google
driver.get("https://google.com")

# 2. Find the search text box on the page using its DOM 'name' attribute
# (This utilizes the DOM selectors you practiced earlier!)
search_box = driver.find_element(By.NAME, "q")

# 3. Type text into the field automatically
search_box.send_keys("Selenium automation testing jobs in Pune")

# 4. Press the Enter key on the virtual keyboard
search_box.send_keys(Keys.ENTER)

print("Success! Search executed automatically.")

# Wait 5 seconds to look at the search results page
time.sleep(5)
driver.quit()
