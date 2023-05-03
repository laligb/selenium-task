from selenium.webdriver.common.by import By

class MainLocators(object):
    link_text = (By.LINK_TEXT, "Challenging DOM")
    table_row = (By.XPATH, "//*[@id='content']/div/div/div/div[2]/table/tbody/tr[1]")
