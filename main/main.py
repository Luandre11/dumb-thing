import pyautogui
import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import random 


#global variables with the driver information
emojis = [":basil_cheer:", ":basil_uneasy:", ":basil_bruh:", ":basil_cry:"]
path = "C:/Program Files (x86)/chromedriver.exe"
driver = webdriver.Chrome(path)
driver.get("https://randomwordgenerator.com/fact.php")


def getIt() -> str:
    """gets the random fact from the website"""
    fact = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "support-sentence")))
    return fact.text
  

def autoGui(text) -> None:
    """types the given text"""
    pyautogui.typewrite(f"Random fact: {text}", interval = 0.1)
    pyautogui.press("enter")


def main() -> None:
    """main function for the random facts"""
    try:
        while "Gay":
            autoGui(f"{getIt()} {random.choice(emojis)}")
            button = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "btn_submit_generator")))
            button.click()
            time.sleep(10)
    except Exception as exc:
        driver.quit()
        raise exc 

if __name__ == "__main__":
    main()




