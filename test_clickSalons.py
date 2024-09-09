import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

from pageObjects.HomePage import HomePage
from utilities.BaseClass import BaseClass



class TestTwo(BaseClass):

    def test_e2e(self):






        homePage = HomePage(self.driver)
        #time.sleep(5)

        homePage.closePromoMet().click()
        #time.sleep(5)
        homePage.acceptAllertCookiesMet().click()
        #time.sleep(5)
        homePage.salonsMet().click()
        #time.sleep(5)
        assert homePage.salonyTextMet().is_displayed()
        #time.sleep(5)


        assert "Salony" in homePage.salonyTextMet().text
        time.sleep(5)

        homePage.searchSalonMet().send_keys("Wrocław")
        time.sleep(5)


        dropdown = Select(self.driver.find_element(By.ID, "radius-select"))
        dropdown.select_by_visible_text("50 km")

        time.sleep(7)
        homePage.searchInMapsMet().click()