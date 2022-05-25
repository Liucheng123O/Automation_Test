import pytest

from JiaoZiDT_Web_PO.PageObjects.home_page import HomePage


@pytest.fixture()
def init_city_dining(init_driver):
    HomePage(init_driver).city_dining_home()

    yield init_driver
    # driver.quit()
