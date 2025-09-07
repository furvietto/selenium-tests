from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def test_duckduckgo_search():
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")

    driver = webdriver.Chrome(options=options)
    wait = WebDriverWait(driver, 10)

    driver.get("https://duckduckgo.com/")
    search_box = wait.until(EC.element_to_be_clickable((By.NAME, "q")))
    search_box.send_keys("Selenium testing")
    search_button = wait.until(EC.element_to_be_clickable(
        (By.CSS_SELECTOR, ".iconButton_button__A_Uiu.searchbox_searchButton__LxebD")
    ))
    search_button.click()

    wait.until(EC.title_contains("Selenium"))
    assert "Selenium" in driver.title

    time.sleep(2)   # giusto per vedere il risultato
    driver.quit()