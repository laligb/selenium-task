## Run selenium and chrome driver to scrape data from cloudbytes.dev
import os.path
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

# Set options for WSL system:

## Setup chrome options
chrome_options = Options()
chrome_options.add_argument("--headless") # Ensure GUI is off
chrome_options.add_argument("--no-sandbox")

# Set path to chromedriver as per your configuration
homedir = os.path.expanduser("~")
webdriver_service = Service(f"{homedir}/chromedriver/stable/chromedriver")
driver = webdriver.Chrome(service=webdriver_service, options=chrome_options)

# Without WSL, by using windows:
# driver = webdriver.Chrome(service=ChromeDriverManager().install())

# Get testing website
driver.get("https://the-internet.herokuapp.com/")
