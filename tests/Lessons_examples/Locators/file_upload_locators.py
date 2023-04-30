from selenium.webdriver.common.by import By

class MainLocators(object):

    link_text = (By.LINK_TEXT, "File Upload")
    file_upload = (By.ID, "file-upload")
    file_submit = (By.ID,"file-submit")
    success = "File Uploaded!"
