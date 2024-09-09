import inspect
import logging
from configparser import ConfigParser

import pytest
from selenium.webdriver.common.by import By

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait




@pytest.mark.usefixtures("setup")

class BaseClass:

    def getLogger(self):
        loggerName = inspect.stack()[1][3]
        logger = logging.getLogger(loggerName)
        fileHandler = logging.FileHandler('logfile.log')
        formatter = logging.Formatter("%(asctime)s :%(levelname)s : %(name)s : %(message)s")
        fileHandler.setFormatter(formatter)

        logger.addHandler(fileHandler)
        logger.setLevel(logging.DEBUG)
        return logger

    def verifyLinkPresence(self,text):
        element = WebDriverWait(self.driver,10).until(EC.presence_of_element_located((By.LINK_TEXT, text)))
        
    
    def selectOptionByText(self, locator, text):
        sel = Select(locator)
        sel.select_by_visible_text(text)

        # w teście: self.selectOptionByText(homepage.getGender(), "Male")

    def read_configuration(category, key):
        config = ConfigParser()
        config.read("configurations/config.ini")
        return config.get(category, key)

