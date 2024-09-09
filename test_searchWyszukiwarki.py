import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

from TestData.HomePageData import HomePageData
from pageObjects.HomePage import HomePage
from utilities.BaseClass import BaseClass



class TestOne(BaseClass):

    def test_e2e(self,getDataTest):
        time.sleep(5)
        # dodajemy obiekt:
        homePage = HomePage(self.driver)
        homePage.closePromoMet().click()
        #time.sleep(5)
        homePage.acceptAllertCookiesMet().click()

        #time.sleep(7)
        homePage.searchMet().send_keys(getDataTest["item"])
        #time.sleep(5)
        homePage.clickSearchMet().click()
        #time.sleep(5)
        homePage.colorItemMet().click()
        #time.sleep(5)
        self.driver.refresh()

    @pytest.fixture(params=HomePageData.test_HomePage_data)
    def getDataTest(self, request):
        return request.param




