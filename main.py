from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from datetime import datetime

while True:
    url = "https://toir.us/"
    options = webdriver.ChromeOptions()
    # The headless version may have some bugs. If you encounter an error while using it, simply add a # symbol at the beginning of the line again.                                                                                                                                                                                                                                                                                                                                                                                  made by maXoz
    #options.add_argument("--headless=chrome")
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    driver = webdriver.Chrome(options=options)
    driver.get(url)
    wait = WebDriverWait(driver, 20)
    element = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".njt-nofi-text.njt-nofi-padding-text strong")))
    version_text = element.text
    version = version_text.split(" ")[1]
    driver.quit()
    try:
        with open("version.txt", "r") as f:
            current_version = f.read()
    except FileNotFoundError:
        current_version = input("Enter the current ToirScript version: ")
        with open("version.txt", "w") as f:
            f.write(current_version)

    if current_version != version:
        current_version = input("Download and enter the new ToirScript version: ")
        with open("version.txt", "w") as f:
            f.write(current_version)
    else:
        print(datetime.now().strftime("%Y-%m-%d %H:%M:%S"), "You are using the latest ToirScript version.")
    time.sleep(300)
