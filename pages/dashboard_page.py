'''from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class DashboardPage(BasePage):
    UPLOAD_INPUT = (By.XPATH, "//input[@type='file']")
    SUCCESS_TEXT = (By.XPATH, "//*[contains(text(),'success')] | //*[contains(text(),'uploaded')] ")
    ERROR_TEXT = (By.XPATH, "//*[contains(text(),'error')] | //*[contains(text(),'invalid')] ")
    SEGMENT_FILTER = (By.XPATH, "//div[contains(text(),'Segment')]")


def upload_file(self, file_path):
    upload = self.wait_for_element(self.UPLOAD_INPUT)
    upload.send_keys(file_path)


def is_upload_successful(self):
    return self.wait_for_element(self.SUCCESS_TEXT).is_displayed()


def is_error_displayed(self):
    return self.wait_for_element(self.ERROR_TEXT).is_displayed()
    '''

'''from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
import time

class DashboardPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 20)
        self.driver.get("http://localhost:8501")  # Streamlit default

    # ---------- LOCATORS ----------
    FILE_UPLOAD = (By.XPATH, "//input[@type='file']")
    SEGMENT_DROPDOWN = (By.XPATH, "//div[contains(@class,'stSelectbox')]")
    SUCCESS_TEXT = (By.XPATH, "//*[contains(text(),'Upload successful')]")
    ERROR_TEXT = (By.XPATH, "//*[contains(text(),'Revenue')]")

    # ---------- ACTIONS ----------
    def upload_file(self, relative_path):
        """
        Uploads an Excel file to Streamlit file_uploader
        """
        absolute_path = os.path.abspath(relative_path)

        upload_element = self.wait.until(
            EC.presence_of_element_located(self.FILE_UPLOAD)
        )

        upload_element.send_keys(absolute_path)
        time.sleep(2)  # Streamlit rerun delay

    def has_upload_error(self):
        return len(self.driver.find_elements(*self.ERROR_TEXT)) > 0

    def is_dashboard_loaded(self):
        return len(self.driver.find_elements(*self.SEGMENT_DROPDOWN)) > 0
'''

'''
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
import time

class DashboardPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 20)
        self.driver.get("http://localhost:8501")  # Streamlit app URL

    # ---------- LOCATORS ----------
    FILE_UPLOAD = (By.XPATH, "//input[@type='file']")
    SUCCESS_TEXT = (By.XPATH, "//*[contains(text(),'Upload successful')]")
    ERROR_TEXT = (By.XPATH, "//*[contains(text(),'Revenue')]")

    # ---------- ACTIONS ----------
    def upload_file(self, relative_path):
        """
        Uploads an Excel file to Streamlit file_uploader
        """
        absolute_path = os.path.abspath(relative_path)
        upload_element = self.wait.until(
            EC.presence_of_element_located(self.FILE_UPLOAD)
        )
        upload_element.send_keys(absolute_path)
        time.sleep(2)  # Streamlit rerun delay

    # ---------- HELPERS ----------
    def wait_for_element(self, locator, timeout=10):
        """Waits for element to appear and returns it"""
        return WebDriverWait(self.driver, timeout).until(
            EC.presence_of_element_located(locator)
        )

    def is_error_displayed(self):
        """Returns True if upload error is visible"""
        return len(self.driver.find_elements(*self.ERROR_TEXT)) > 0

    def is_upload_successful(self):
        """Returns True if success message is visible"""
        return len(self.driver.find_elements(*self.SUCCESS_TEXT)) > 0
'''

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
import time

class DashboardPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 30)
        self.driver.get("http://localhost:8501")  # Streamlit URL

    FILE_UPLOAD = (By.XPATH, "//input[@type='file']")
    SUCCESS_TEXTS = ["Upload successful", "File uploaded successfully", "Processing complete"]
    ERROR_TEXTS = ["Revenue", "Error"]

    def upload_file(self, relative_path):
        absolute_path = os.path.abspath(relative_path)
        upload_element = self.wait.until(EC.presence_of_element_located(self.FILE_UPLOAD))
        upload_element.send_keys(absolute_path)
        time.sleep(3)  # wait for Streamlit rerun

    def wait_for_element(self, locator, timeout=20):
        """Waits for element to appear and returns it"""
        return WebDriverWait(self.driver, timeout).until(
            EC.presence_of_element_located(locator)
        )

    def is_upload_successful(self):
        """Returns True if any known success message is visible"""
        for msg in self.SUCCESS_TEXTS:
            if self.driver.find_elements(By.XPATH, f"//*[contains(text(),'{msg}')]"):
                return True
        return False

    def is_error_displayed(self):
        """Returns True if any known error message is visible"""
        for msg in self.ERROR_TEXTS:
            if self.driver.find_elements(By.XPATH, f"//*[contains(text(),'{msg}')]"):
                return True
        return False

    def wait_for_text(self, text, timeout=20):
        """Wait for arbitrary text to appear"""
        return WebDriverWait(self.driver, timeout).until(
            EC.presence_of_element_located((By.XPATH, f"//*[contains(text(),'{text}')]"))
        )
