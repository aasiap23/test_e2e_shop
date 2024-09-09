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

from pageObjects.AssetionsPage import AssertionsPage
from pageObjects.HomePage import HomePage
from utilities.BaseClass import BaseClass





class TestFive(BaseClass):
    def test_e2e(self):
        log = self.getLogger()
        homePage = HomePage(self.driver)
        time.sleep(5)
        homePage.closePromoMet().click()
        log.info("close promo")
        time.sleep(5)
        homePage.acceptAllertCookiesMet().click()
        log.info("accept cookies")
        time.sleep(5)

    def test_assert(self):
        assertionsPage = AssertionsPage(self.driver)
        time.sleep(5)
        assert assertionsPage.promo10Met().is_displayed()
        time.sleep(5)
        assert "DODATKOWE 10% RABATU - POBIERZ APLIKACJĘ" in assertionsPage.promo10Met().text
        time.sleep(5)
        assert "Rekomendowane dla Ciebie!" in assertionsPage.rekoMet().text
        time.sleep(5)
        assert "Homla – Sklep z wyposażeniem wnętrz | Homla.com.pl" in self.driver.title
        time.sleep(10)
        assert assertionsPage.newsletterIsDisplayeMet().is_displayed()
        time.sleep(5)
        assert "Bestsellery" == assertionsPage.bestsellersMet().text
        time.sleep(5)
        assert len(assertionsPage.reko2Met()) == 1
        time.sleep(5)
        assert not self.driver.find_elements(By.ID, "nieistniejacyElement")
        time.sleep(5)



