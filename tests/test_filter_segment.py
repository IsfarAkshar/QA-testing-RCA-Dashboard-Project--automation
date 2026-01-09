from pages.dashboard_page import DashboardPage
from selenium.webdriver.common.by import By


def test_filter_segment(driver):
    dashboard = DashboardPage(driver)
    dashboard.upload_file("test_data/kpi_valid.xlsx")
    segment = dashboard.wait_for_element((By.XPATH, "//*[text()='Prepaid']"))
    segment.click()
    assert segment.is_displayed()