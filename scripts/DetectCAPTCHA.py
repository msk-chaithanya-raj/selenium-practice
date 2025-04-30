from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get("https://www.google.com/recaptcha/api2/demo")

# STEP 1: Detect CAPTCHA
try:
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//iframe[contains(@src, 'recaptcha')]"))
    )
    print("🛑 CAPTCHA detected — waiting for you to solve it manually...")
    
    # STEP 2: Pause script to let human solve CAPTCHA
    input("✅ After solving CAPTCHA, press Enter to continue...")
    captcha_iframe = driver.find_elements(By.XPATH, "//iframe[contains(@src, 'recaptcha')]")
    if not captcha_iframe:
        print("✅ CAPTCHA solved (iframe disappeared)")
    else:
        print("⚠️ CAPTCHA still active — maybe not solved yet.")

except:
    print("✅ No CAPTCHA found — continuing...")
