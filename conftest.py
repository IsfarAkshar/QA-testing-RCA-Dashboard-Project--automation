#import pytest
#from selenium import webdriver
#from selenium.webdriver.chrome.service import Service
#from webdriver_manager.chrome import ChromeDriverManager


#@pytest.fixture(scope="function")
#def driver():
#    options = webdriver.ChromeOptions()
#    options.add_argument("--start-maximized")
#    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
#    driver.get("http://localhost:8501") # Streamlit app URL
#    yield driver
#    driver.quit()

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import os

@pytest.fixture(scope="function")
def driver():
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")

    driver_path = ChromeDriverManager().install()

    # 🔴 FIX: ensure we use chromedriver.exe, not THIRD_PARTY_NOTICES
    if not driver_path.endswith("chromedriver.exe"):
        driver_path = os.path.join(os.path.dirname(driver_path), "chromedriver.exe")

    service = Service(driver_path)
    driver = webdriver.Chrome(service=service, options=options)

    yield driver
    driver.quit()
