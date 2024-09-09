import time
from telnetlib import EC

from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from TestData.HomePageData import HomePageData
from pageObjects.HomePage import HomePage
from pageObjects.NewsPage import NewsPage
from utilities.BaseClass import BaseClass

class TestFour(BaseClass):
    def test_e2e(self):
        log =  self.getLogger()
        homePage = HomePage(self.driver)
        time.sleep(5)
        homePage.closePromoMet().click()
        log.info("close promo")
        time.sleep(5)
        homePage.acceptAllertCookiesMet().click()
        log.info("accept cookies")
        time.sleep(5)


    def test_e2e2(self):
        log = self.getLogger()
        newsPage = NewsPage(self.driver)
        time.sleep(15)
        newsPage.newsMet().click()
        log.info("click on news section")
        time.sleep(5)
        action = ActionChains(self.driver)

        action.move_to_element(self.driver.find_element(By.XPATH,
                                                        "//div[contains(text(),'Cena')]")).perform()
        time.sleep(5)
        action.click(self.driver.find_element(By.XPATH,
                                                     "//div[contains(text(),'Cena')]")).perform()

        time.sleep(5)



        slider = self.driver.find_element(By.XPATH, "//div[contains(@data-role,'range-price-slider-price')]//a[1]")

        # Pobierz szerokość slidera
        slider_width = slider.size['width']

        # Ustaw wartość, na którą chcesz przesunąć slider (np. 50%)
        desired_value = 50

        # Oblicz docelową pozycję slidera
        target_position = slider_width * desired_value / 90

        # Inicjalizacja obiektu ActionChains
        actions = ActionChains(self.driver)

        # Przesuń slider do docelowej pozycji
        actions.click_and_hold(slider).move_by_offset(target_position, 0).release().perform()
        time.sleep(5)

        slider = self.driver.find_element(By.XPATH, "//div[contains(@data-role,'range-price-slider-price')]//a[2]")

        # Pobierz szerokość slidera
        slider_width = slider.size['width']

        # Ustaw wartość, na którą chcesz przesunąć slider (np. 50%)
        desired_value = -50

        # Oblicz docelową pozycję slidera
        target_position = slider_width * desired_value /30

        # Inicjalizacja obiektu ActionChains
        actions = ActionChains(self.driver)

        # Przesuń slider do docelowej pozycji
        actions.click_and_hold(slider).move_by_offset(target_position, 0).release().perform()
        time.sleep(5)

        newsPage.confirmPriceMet().click()
        time.sleep(5)


        time.sleep(5)
        action = ActionChains(self.driver)
        action.move_to_element(self.driver.find_element(By.XPATH,
                                                        "//div[normalize-space()='Kolor']")).perform()
        time.sleep(5)
        action.click(self.driver.find_element(By.XPATH,
                                                     "//div[normalize-space()='Kolor']")).perform()

        time.sleep(5)

        newsPage.blackColorMet().click()
        time.sleep(5)
        newsPage.confirmColorMet().click()
        time.sleep(5)

        action = ActionChains(self.driver)

        time.sleep(5)
        action.click(self.driver.find_element(By.LINK_TEXT,
                                              "Szafka nocna SOMBRE lite drewno mango żłobione 45x45x60 cm")).perform()

        time.sleep(5)

        newsPage.quantityMet().click()
        time.sleep(5)

        newsPage.addToCartMet_and_goToCartMet().click()
        time.sleep(5)

        #newsPage.goToCartMet().click()
        #time.sleep(5)

