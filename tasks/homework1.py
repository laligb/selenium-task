from tasks.driver import *
import time
import os

# Check current URL:
print(driver.current_url)
driver.find_element(By.LINK_TEXT, "File Upload").click()

# Check current URL after the command:
print(driver.current_url)

file_path = os.path.abspath("images/khinkali.jpg")
print(file_path)
driver.find_element(By.ID, "file-upload").send_keys(file_path)
driver.find_element(By.ID,"file-submit").submit()

try:
    assert driver.page_source.find("File Uploaded!")
    time.sleep(5)
    print("file upload success")
except:
    print("file upload not successful")

driver.quit()
