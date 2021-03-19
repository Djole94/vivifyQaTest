from selenium import webdriver
import pytest
from time import sleep
from chromedriver_py import binary_path


class TestGalleryApp:

    @pytest.fixture()
    def setUp(self):
        global driver
        driver = webdriver.Chrome(executable_path=binary_path)
        # driver = webdriver.Chrome("../drivers/chromedriver.exe")
        driver.implicitly_wait(30)
        driver.maximize_window()
        # go to web app page
        driver.get("https://gallery-app.vivifyideas.com/")

    # check to see if we are on home page
    def test_1(self, setUp):
        sleep(1)

        assert (driver.current_url == "https://gallery-app.vivifyideas.com/")