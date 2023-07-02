import time

import pytest
from pageObjects.LoginPage import LoginPage
from pageObjects.AddCustomerPage import AddCustomer
from pageObjects.SearchCustomerPage import SearchCustomer
from utilities.readProperties import ReadConfig as config
from utilities.customLogger import Logs

class Test_SearchCustomerByEmail_004():
    baseURL = config.getApplicationURL()
    username = config.getUserName()
    password = config.getPassword()
    logger = Logs.getLogs() #Logger

    @pytest.mark.regression
    def test_SearchCustomerByEmail(self,setup):
        self.logger.info("************* SearchCustomerByEmail_0004 **************")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.login = LoginPage(self.driver)
        self.login.setUserName(self.username)
        self.login.setPassword(self.password)
        self.login.clickLogin()

        self.logger.info("*********** Login Successfull **********")

        self.logger.info("********* Starting Search Customer By Email... *************")

        self.addCust = AddCustomer(self.driver)
        self.addCust.clickOnCustomersMenu()
        self.addCust.clickOnCustomersMenuItem()

        self.logger.info("********* Searching Customer By Email ID ************")

        searchCustomer = SearchCustomer(self.driver)
        searchCustomer.setEmail("victoria_victoria@nopCommerce.com")
        searchCustomer.clickSearch()
        time.sleep(5)
        status = searchCustomer.searchCustomerByEmail("victoria_victoria@nopCommerce.com")
        assert True == status
        self.logger.info("******* TC_SearchCustomerByEmail_004 Finished *************")
        self.driver.close()