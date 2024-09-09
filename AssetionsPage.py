from selenium.webdriver.common.by import By


class AssertionsPage:

    def __init__(self, driver):
        self.driver = driver
        self.driver.implicitly_wait(10)

    promo10 = (By.CSS_SELECTOR, ".odliczanie-belka-span")
    reko = (By.CSS_SELECTOR, ".snrs-reco-title")
    newsletterIsDisplaye = (By.CLASS_NAME, "title")
    bestsellers = (By.XPATH, "//a[normalize-space()='Bestsellery']")

    def promo10Met(self):
        return self.driver.find_element(*AssertionsPage.promo10)

    def rekoMet(self):
        return self.driver.find_element(*AssertionsPage.reko)

    def reko2Met(self):
        return self.driver.find_elements(*AssertionsPage.reko)

    def newsletterIsDisplayeMet(self):
        return self.driver.find_element(*AssertionsPage.newsletterIsDisplaye)

    def bestsellersMet(self):
        return self.driver.find_element(*AssertionsPage.bestsellers)

