from selenium.webdriver.common.by import By

class MainLocators(object):

    link_text = (By.LINK_TEXT, "Shifting Content")
    link_text_example1 = (By.LINK_TEXT, "Example 1: Menu Element")
    link_text_home = (By.LINK_TEXT, "Home")
    link_text_example2 = (By.LINK_TEXT, "Example 2: An image")
    link_of_image = (By.CSS_SELECTOR, "[href^=/shifting_content/image]")
    image_link = (By.CLASS_NAME, "shift")
    position_of_image = (By.CLASS_NAME, "shift").value_of_css_property('left')
