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


class TestThree(BaseClass):
    def test_e2e(self, getDataTest):
        time.sleep(5)
        log = self.getLogger()

        homePage = HomePage(self.driver)
        time.sleep(5)
        homePage.closePromoMet().click()
        time.sleep(5)
        homePage.acceptAllertCookiesMet().click()
        time.sleep(5)
        homePage.myaccountMet().click()
        time.sleep(5)
        homePage.newAccountMet().click()
        time.sleep(5)
        homePage.nameMet().send_keys(getDataTest["name"])
        log.info("check the first name:" + getDataTest["name"])
        time.sleep(5)
        homePage.surnameMet().send_keys(getDataTest["surname"])
        time.sleep(5)
        self.driver.refresh()

    @pytest.fixture(params=HomePageData.test_Account_data)
    def getDataTest(self, request):
        return request.param




