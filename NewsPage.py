from selenium.webdriver.common.by import By


class NewsPage:
    #konstruktor init dla drivera z testu e2e
    def __init__(self, driver):
        self.driver = driver
        self.driver.implicitly_wait(10)

    news = (By.CSS_SELECTOR, "li[id='menu4524'] a:nth-child(1)")
    confirmPrice = (By.XPATH, "//div[contains(@aria-hidden,'false')]//span[contains(text(),'Zatwierdź')]")
    blackColor = (By.XPATH, "//label[@for='colorFilter_option_2']")
    confirmColor = (By.XPATH, "//div[@aria-hidden='false']//span[contains(text(),'Zatwierdź')]")
    quantity = (By.XPATH, "//span[normalize-space()='+']")
    addToCart = (By.XPATH, "//span[normalize-space()='Dodaj do koszyka']")
    goToCart = (By.XPATH, "//button[@type='button']//span[contains(text(),'Przejdź do koszyka')]")



    def newsMet(self):
        return self.driver.find_element(*NewsPage.news)

    def confirmPriceMet(self):
        return self.driver.find_element(*NewsPage.confirmPrice)

    def blackColorMet(self):
        return self.driver.find_element(*NewsPage.blackColor)

    def confirmColorMet(self):
        return self.driver.find_element(*NewsPage.confirmColor)

    def quantityMet(self):
        return self.driver.find_element(*NewsPage.quantity)

    def addToCartMet_and_goToCartMet(self):
        return self.driver.find_element(*NewsPage.addToCart)
        return self.driver.find_element(*NewsPage.goToCart)

    #def goToCartMet(self):
    #    return self.driver.find_element(*NewsPage.goToCart)