from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get("https://the-internet.herokuapp.com/login")

# Wait for the login form to load
WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, "username"))
)

# Fill the form
driver.find_element(By.ID, "username").send_keys("tomsmith")
driver.find_element(By.ID, "password").send_keys("SuperSecretPassword!")
driver.find_element(By.CSS_SELECTOR, "button.radius").click()

# Wait for success message
WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CLASS_NAME, "flash.success"))
)

print("✅ Login successful!")

driver.quit()
