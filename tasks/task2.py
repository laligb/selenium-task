from tasks.task1 import *
from selenium.webdriver.support.select import Select



print("Task # 2: cheking dropdown ")

driver.back()

print(driver.current_url)
driver.find_element(By.LINK_TEXT, "Dropdown").click()
print(driver.current_url)

# Select the Option #2
select_element = driver.find_element(By.ID, 'dropdown')
print(select_element)
select = Select(select_element)
print(select)


select.select_by_visible_text('Option 2')
print(len(select.all_selected_options))
# assert "Option 2" in select.all_selected_options
driver.quit()
