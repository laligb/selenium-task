from tasks.driver import *
import time
import os

# Task # 1
print("Task #1: cheking file uploading")

# Check current URL:
print(driver.current_url)
driver.find_element(By.LINK_TEXT, "File Upload").click()

# Check current URL after the command:
print(driver.current_url)

def upload_file(file_name):
    try:
        file_path = os.path.abspath(file_name)
        print(file_path)
        driver.find_element(By.ID, "file-upload").send_keys(file_path)
        driver.find_element(By.ID,"file-submit").submit()
        try:
            assert driver.page_source.find("File Uploaded!")
            time.sleep(5)
            print("file upload success")
        except:
            print("file upload not successful")

    except:
        print("File does not exist in the path")


# Successful upload testing
upload_file("images/khinkali.jpg")

# Unsuccessful upload testing
driver.back()
print(driver.current_url)
upload_file("hello.jpg")
