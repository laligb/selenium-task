from tests.task1.test_uploading import *
from selenium.webdriver.support.select import Select

print("---")
print("Task # 2: checking dropdown ")

driver.back()

print(driver.current_url)
driver.find_element(By.LINK_TEXT, "Dropdown").click()
print(driver.current_url)

# Select the Option #2
select = Select(driver.find_element(By.ID, 'dropdown'))
select.select_by_visible_text('Option 2')
selected = select.first_selected_option.get_attribute("text")
print("")
print(selected)
try:
    assert 'Option 2' in selected
    print("selected correctly")
except:
    print("Wrong selection")

# Second part - go to redirect link
print("---")
try:
    driver.back()
    print(driver.current_url)
    driver.find_element(By.LINK_TEXT, "Redirect Link").click()
    print(driver.current_url)
    try:
        assert "https://the-internet.herokuapp.com/redirector" in driver.current_url
        print("Correct redirection")
    except:
        print("incorrect redirection")
except:
    print("Something wrong with the link")


# Finishing:
print("Test finished!")
driver.quit()
