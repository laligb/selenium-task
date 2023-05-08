from selenium.webdriver.common.by import By

class MainLocators(object):
    link_text = (By.LINK_TEXT, "Key Presses")
    input_field = (By.ID, "target")
    result = (By.ID, "result")
