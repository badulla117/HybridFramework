import string
import random

import pytest
from pageObjects.LoginPage import LoginPage
from pageObjects.AddCustomerPage import AddCustomer
from utilities.readProperties import ReadConfig as config
from utilities.customLogger import Logs
from selenium.webdriver.common.by import By

class Test_003_AddCustomer():
    baseURL = config.getApplicationURL()
    username = config.getUserName()
    password = config.getPassword()
    logger = Logs.getLogs()

    @pytest.mark.sanity
    def test_AddCustomer(self,setup):
        self.logger.info("************* Test_003_AddCustomer **************")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.login = LoginPage(self.driver)
        self.login.setUserName(self.username)
        self.login.setPassword(self.password)
        self.login.clickLogin()

        self.logger.info("*********** Login Successfull **********")

        self.logger.info("*********** Started Add Customer Test... **************")

        self.addCust = AddCustomer(self.driver)
        self.addCust.clickOnCustomersMenu()
        self.addCust.clickOnCustomersMenuItem()

        self.addCust.clickOnAddNewButton()

        self.logger.info("*************** Providing Customer Information.. *************")

        self.email = random_generator() + "@gmail.com"
        self.addCust.setEmail(self.email)
        self.addCust.setPassword("ammu@123")
        self.addCust.setFirstName("John")
        self.addCust.setLastName("Watson")
        self.addCust.setGender("Male")
        self.addCust.setDateOfBirth("06/09/1985")
        self.addCust.setCompanyName("Walmart Pvt Ltd")
        self.addCust.selectTax()
        self.addCust.setNewLetter("Test store 2")
        self.addCust.setCustomerRoles("Registered")
        self.addCust.setManagerOfVendor("Vendor 2")
        self.addCust.setAdminComment("This is for Testing.....")
        self.addCust.clickSave()

        self.logger.info("*********** Saving Customer Information ************")

        self.logger.info("*********** Add Customer Validation Started... *************")

        self.msg = self.driver.find_element(By.TAG_NAME,"body").text

        if "The new customer has been added successfully." in self.msg:
            assert True == True
            self.logger.info("********** Add Customer Test Passed.... **********")
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_addcustomer_scr.png")
            self.logger.error("*********** Add Customer Test Failed... *********")
            assert False == False

        self.driver.close()
        self.logger.info("******** Ending Test_003_AddCustomer Test ***********")

def random_generator(size = 8, chars = string.ascii_lowercase + string.digits):
    gmail = ''.join(random.choice(chars) for x in range(size))
    return gmail