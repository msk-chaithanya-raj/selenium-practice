from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import time

options = Options()
options.add_argument("--headless")
options.add_argument("--disable-gpu")
driver = webdriver.Chrome(options=options)
driver.get("https://the-internet.herokuapp.com/login")

# Wait for the login form to load
WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, "username"))
)

# Fill the form
driver.find_element(By.ID, "username").send_keys("tomsmith")
driver.find_element(By.ID, "password").send_keys("SuperSecretPassword!")
# driver.find_element(By.ID, "password").send_keys("csancknaclk!")
driver.find_element(By.CSS_SELECTOR, "button.radius").click()


time.sleep(1)

message = driver.find_element(By.ID, "flash").text

if "You logged into a secure area!" in message:
    # Wait for success message
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "flash.success"))
    )
    print("✅ SUCCESS: Logged in")
elif "Your username is invalid!" in message:
    print("❌ ERROR: Invalid username")
elif "Your password is invalid!" in message:
    print("❌ ERROR: Invalid password")
else:
    print("⚠️ Unknown result")


driver.quit()
