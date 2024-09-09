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

from pageObjects.HomePage import HomePage
from utilities.BaseClass import BaseClass

class TestTwo(BaseClass):

    def test_e2e(self):

        time.sleep(5)



        homePage = HomePage(self.driver)
        time.sleep(5)
        homePage.closePromoMet().click()
        time.sleep(5)
        homePage.acceptAllertCookiesMet().click()
        time.sleep(5)

        action = ActionChains(self.driver)
        action.move_to_element(self.driver.find_element(By.XPATH, "//a[@class='mega has-child dynamic-width']//span[@class='menu-title'][normalize-space()='Salon']")).perform()
        time.sleep(5)
        action.double_click(self.driver.find_element(By.CSS_SELECTOR, "li[id='menu4178'] a[class='mega']")).perform()
        time.sleep(7)

        homePage.colorMirrorMet().click()
        time.sleep(5)
        homePage.ecruColorMet().click()





        time.sleep(5)
        homePage.priceAssMet()

