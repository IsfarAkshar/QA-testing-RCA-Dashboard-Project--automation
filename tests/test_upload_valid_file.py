from pages.dashboard_page import DashboardPage


def test_upload_valid_file(driver):
    dashboard = DashboardPage(driver)
    dashboard.upload_file("test_data/kpi_valid.xlsx")
    assert dashboard.is_upload_successful()