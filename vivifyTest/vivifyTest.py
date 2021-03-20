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

    # go to the register page
    def test_2(self):
        driver.find_element_by_xpath("//a[contains(text(),'Register')]").click()
        sleep(0.5)

        assert (driver.current_url == "https://gallery-app.vivifyideas.com/register")

    # user registration
    def test_3(self):
        driver.find_element_by_xpath("//input[@id='first-name']").send_keys("test1")
        sleep(.2)
        driver.find_element_by_xpath("//input[@id='last-name']").send_keys("test1")
        sleep(.2)
        driver.find_element_by_xpath("//input[@id='email']").send_keys("test12@gmail.com")
        sleep(.2)
        driver.find_element_by_xpath("//input[@id='password']").send_keys("12345678")
        sleep(.2)
        driver.find_element_by_xpath("//input[@id='password-confirmation']").send_keys("12345678")
        sleep(.2)
        driver.find_element_by_xpath("//body/div[@id='app']/div[2]/div[1]/form[1]/div[6]/input[1]").click()
        sleep(.2)
        driver.find_element_by_xpath("//button[contains(text(),'Submit')]").click()
        sleep(1)

        assert (driver.find_element_by_xpath("//a[contains(text(),'Logout')]").text == "Logout")

    # logging registered user
    def test_4(self, setUp):
        sleep(1)
        driver.find_element_by_xpath("//a[contains(text(),'Login')]").click()
        sleep(.5)

        assert (driver.current_url == "https://gallery-app.vivifyideas.com/login")

        driver.find_element_by_xpath("//input[@id='email']").send_keys("test1@gmail.com")
        sleep(.2)
        driver.find_element_by_xpath("//input[@id='password']").send_keys("12345678")
        sleep(.2)
        driver.find_element_by_xpath("//button[contains(text(),'Submit')]").click()
        sleep(1)

        assert (driver.find_element_by_xpath("//a[contains(text(),'Logout')]").text == "Logout")

    # create Gallery
    def test_5(self):
        sleep(1)
        driver.find_element_by_xpath("//a[contains(text(),'Create Gallery')]").click()
        sleep(.2)

        assert (driver.current_url == "https://gallery-app.vivifyideas.com/create")

        driver.find_element_by_xpath("//input[@id='title']").send_keys("test1Gallery")
        sleep(.2)
        driver.find_element_by_xpath("//input[@id='description']").send_keys("bla bla bla, neki opis")
        sleep(.2)
        driver.find_element_by_xpath("//body/div[@id='app']/div[2]/div[1]/div[1]/form[1]/div[3]/div[1]/div[1]/input[1]")\
                .send_keys("https://i.pinimg.com/originals/39/ab/4b/39ab4b0edf37852314be7176004e29cb.jpg")
        sleep(.2)
        # driver.find_element_by_xpath("//button[contains(text(),'Add image')]").click()
        # sleep(.2)
        driver.find_element_by_xpath("//button[contains(text(),'Submit')]").click()
        sleep(2)

        assert (driver.current_url == "https://gallery-app.vivifyideas.com/")

    # go to MyGallery page
    def test_6(self):
        sleep(1)
        driver.find_element_by_xpath("//a[contains(text(),'My Galleries')]").click()
        sleep(2)

        assert (driver.current_url == "https://gallery-app.vivifyideas.com/my-galleries")
