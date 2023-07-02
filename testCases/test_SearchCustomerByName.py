import time
import pytest

from pageObjects.LoginPage import LoginPage
from pageObjects.AddCustomerPage import AddCustomer
from pageObjects.SearchCustomerPage import SearchCustomer
from utilities.readProperties import ReadConfig as config
from utilities.customLogger import Logs

class Test_SearchCustomerByName_005():
    baseURL = config.getApplicationURL()
    username = config.getUserName()
    password = config.getPassword()
    logger = Logs.getLogs() #Logger

    @pytest.mark.regression
    def test_SearchCustomerByName(self,setup):
        self.logger.info("************* SearchCustomerByName_005 **************")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.login = LoginPage(self.driver)
        self.login.setUserName(self.username)
        self.login.setPassword(self.password)
        self.login.clickLogin()

        self.logger.info("*********** Login Successfull **********")

        self.logger.info("********* Starting Search Customer By Name... *************")

        self.addCust = AddCustomer(self.driver)
        self.addCust.clickOnCustomersMenu()
        self.addCust.clickOnCustomersMenuItem()

        self.logger.info("********* Searching Customer By Name ************")

        searchCustomer = SearchCustomer(self.driver)
        searchCustomer.setFirstName("Brenda")
        searchCustomer.setLastName("Lindgren")
        searchCustomer.clickSearch()
        time.sleep(5)
        status = searchCustomer.searchCustomerByName("Brenda Lindgren")
        assert True == status
        self.logger.info("******* TC_SearchCustomerByName_005 Finished *************")
        self.driver.close()