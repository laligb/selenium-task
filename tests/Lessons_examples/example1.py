from tests.task1.driver import *
import time

# Task # 1 from lesson:

driver.find_element(By.LINK_TEXT, "Form Authentication").click()
driver.find_element(By.ID, "username").send_keys("12")
driver.find_element(By.ID, "password").send_keys("SuperSecretPassword!")
driver.find_element(By.CLASS_NAME, "radius").click()
driver.find_element(By.CSS_SELECTOR, ".radius > i").click()
print(driver)

try:

    success_result = driver.find_element(By.ID, "flash").text
    assert "You logged into a secure area!" in success_result
    time.sleep(5)

except:
    print("Unsuccessful result")
