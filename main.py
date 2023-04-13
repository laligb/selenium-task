
## Run selenium and chrome driver to scrape data from cloudbytes.dev
import time
import os.path
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options


## Setup chrome options
chrome_options = Options()
chrome_options.add_argument("--headless") # Ensure GUI is off
chrome_options.add_argument("--no-sandbox")

# Set path to chromedriver as per your configuration
homedir = os.path.expanduser("~")

webdriver_service = Service(f"{homedir}/chromedriver/stable/chromedriver")

driver = webdriver.Chrome(service=webdriver_service, options=chrome_options)

#driver = webdriver.Chrome(service=ChromeDriverManager().install())
#driver = webdriver.Chrome('/path/to/chromedriver')

# driver = webdriver.Remote(
#     command_executor='http://127.0.0.1:5500',
#     desired_capabilities=DesiredCapabilities.CHROME)


driver.get("https://the-internet.herokuapp.com/")

try:
    driver.find_element(By.LINK_TEXT, "Form Authentication").click()
    driver.find_element(By.ID, "username").send_keys("12")
    driver.find_element(By.ID, "password").send_keys("SuperSecretPassword!")
    driver.find_element(By.CLASS_NAME, "radius").click()
    driver.find_element(By.CSS_SELECTOR, ".radius > i").click()
    print(driver)

    success_result = driver.find_element(By.ID, "flash").text
    assert "You logged into a secure area!" in success_result
    time.sleep(5)

except:
    print("something is wrong")

# print(driver.get_cookies())
# driver.add_cookie({})

# driver.back()

# start = driver.find_element(By.ID)
# target = driver.find_element(By.ID)
