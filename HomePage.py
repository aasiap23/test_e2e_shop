from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.common.by import By

class HomePage:
    #konstruktor init dla drivera z testu e2e
    def __init__(self, driver):
        self.driver = driver
        self.driver.implicitly_wait(10)

    acceptAllertCookies = (By.ID, "CybotCookiebotDialogBodyLevelButtonLevelOptinAllowAll")

    closePromo =(By.ID,"snrs-modal-popup-close-new")
    search =(By.ID,"search")
    clickSearch=(By.CSS_SELECTOR, "button[title='Szukaj']")
    colorItem =(By.LINK_TEXT, "Lustro wiszące CLARA ozdobne 50 cm")

    salons = (By.CLASS_NAME, "shops-link__link")
    searchSalon = (By.ID, "mw-sl_search_text")
    searchInMaps = (By.CLASS_NAME, "mw-sl__search__submit")
    detailsSearch= (By.ID, "72")
    salonyText = (By.LINK_TEXT, "Salony")

    colorMirror =(By.XPATH, "//div[normalize-space()='Kolor']")
    ecruColor = (By.XPATH, "//label[@for='colorFilter_option_1']")
    buttonZatwierdz =(By.XPATH, "//div[@aria-hidden='false']//span[contains(text(),'Zatwierdź')]")


    myaccount = (By.XPATH, "//a[@class='action dropdown']")
    newAccount = (By.XPATH, "//a[@class='action create primary button-wider']//span[contains(text(),'Utwórz konto')]")
    name = (By.ID, "firstname")
    surname = (By.ID, "lastname")




    def acceptAllertCookiesMet(self):
        return self.driver.find_element(*HomePage.acceptAllertCookies)

    def closePromoMet(self):
        return self.driver.find_element(*HomePage.closePromo)

    def searchMet(self):
        return self.driver.find_element(*HomePage.search)

    def clickSearchMet(self):
        return self.driver.find_element(*HomePage.clickSearch)

    def colorItemMet(self):
        return self.driver.find_element(*HomePage.colorItem)

    def salonsMet(self):
        return self.driver.find_element(*HomePage.salons)

    def searchSalonMet(self):
        return self.driver.find_element(*HomePage.searchSalon)

    def searchInMapsMet(self):
        return self.driver.find_element(*HomePage.searchInMaps)

    def detailsSearchMet(self):
        return self.driver.find_element(*HomePage.detailsSearch)

    def colorMirrorMet(self):
        return self.driver.find_element(*HomePage.colorMirror)

    def ecruColorMet(self):
        return self.driver.find_element(*HomePage.ecruColor)

    def buttonZatwierdzMet(self):
        return self.driver.find_element(*HomePage.buttonZatwierdz)

    def myaccountMet(self):
        return self.driver.find_element(*HomePage.myaccount)

    def newAccountMet(self):
        return self.driver.find_element(*HomePage.newAccount)

    def nameMet(self):
        return self.driver.find_element(*HomePage.name)

    def surnameMet(self):
        return self.driver.find_element(*HomePage.surname)

    def salonyTextMet(self):
        return self.driver.find_element(*HomePage.salonyText)












