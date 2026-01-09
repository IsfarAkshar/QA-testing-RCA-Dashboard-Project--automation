from pages.dashboard_page import DashboardPage


def test_upload_invalid_file(driver):
    dashboard = DashboardPage(driver)
    dashboard.upload_file("test_data/kpi_missing_revenue.xlsx")
    assert dashboard.is_error_displayed()