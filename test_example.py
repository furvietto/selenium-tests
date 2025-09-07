from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from tempfile import mkdtemp
import os

def test_duckduckgo_search():
    options = webdriver.ChromeOptions()

    if os.getenv("CI"):  # siamo in GitHub Actions
        options.add_argument("--headless=new")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--disable-gpu")
        options.add_argument("--window-size=1920,1080")
        # profilo temporaneo unico
        options.add_argument(f"--user-data-dir={mkdtemp()}")
        chrome_bin = os.getenv("CHROME_BIN")
        if chrome_bin:
            options.binary_location = chrome_bin
    else:  # in locale, finestra normale
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

    driver.quit()