# # type:ignore
# from selenium import webdriver 
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.support.ui import WebDriverWait
# import time

# driver = webdriver.Chrome()
# driver.get("https://web.whatsapp.com/")

# searc_box = WebDriverWait(driver, 60).until(
#     EC.presence_of_element_located((By.XPATH, '//*[@aria-label="Search input textbox"]'))
# )
# searc_box.send_keys("Armish Iftikhar")
# searc_box.send_keys(Keys.RETURN)

# WebDriverWait(driver, 10).until(
#     EC.presence_of_element_located((By.XPATH, '//*[@title="Armish Iftikhar"]'))
# ).click()

# message_box = WebDriverWait(driver, 10).until(
#     EC.presence_of_element_located((By.XPATH, '//*[@aria-label="Type a message"]'))
# )

# message_box.send_keys("Hey Beautiful, you are gorgeous")
# message_box.send_keys(Keys.RETURN)

# time.sleep(10)
# driver.close()


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

# Initialize the driver
driver = webdriver.Chrome()

# Open WhatsApp Web
driver.get("https://web.whatsapp.com/")

# Wait for the search box to be available
search_box = WebDriverWait(driver, 60).until(
    EC.presence_of_element_located((By.XPATH, '//*[@aria-label="Search input textbox"]'))
)
search_box.send_keys("Armish Iftikhar")
search_box.send_keys(Keys.RETURN)

# Wait for the contact to be present and clickable, then click on it
contact = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, '//*[@title="Armish Iftikhar"]'))
)
contact.click()

# Wait for the message box to be available
message_box = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, '//*[@aria-label="Type a message"]'))
)

# Send the message
message_box.send_keys("Hey Beautiful, you are gorgeous")
message_box.send_keys(Keys.RETURN)

# Optionally, wait for a few seconds to observe the message being sent
WebDriverWait(driver, 10).until(
    EC.staleness_of(message_box)  # Wait until the message box becomes stale, indicating the message was sent
)

# Close the driver
driver.quit()
