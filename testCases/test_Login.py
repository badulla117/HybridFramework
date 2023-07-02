import pytest
from pageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig as config
from utilities.customLogger import Logs

class Test_001_Login:
    baseURL = config.getApplicationURL()
    username = config.getUserName()
    password = config.getPassword()
    logger = Logs.getLogs()

    @pytest.mark.regression
    def test_HomePageTitle(self,setup):
        self.logger.info("*************** Test_001_Login ***************")
        self.logger.info("************** Verifying Home Page Title ***************")
        self.driver = setup
        self.driver.get(self.baseURL)
        act_title = self.driver.title
        if act_title == "Your store. Login":
            assert True
            self.logger.info("*************** Home Page Title Test is Passed... ***************")
            self.driver.close()
        else:
            self.driver.save_screenshot(".\\Screenshots\\"+"test_HomePageTitle.png")
            self.logger.error("*************** Home Page Title Test is Failed... ***************")
            assert False
            self.driver.close()

    @pytest.mark.sanity
    def test_Login(self,setup):
        self.logger.info ("*************** Verifying Login Test ***************")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.login = LoginPage(self.driver)
        self.login.setUserName(self.username)
        self.login.setPassword(self.password)
        self.login.clickLogin()
        act_title = self.driver.title
        if act_title == "Dashboard / nopCommerce administration":
            assert True
            self.logger.info("*************** Login Page Title Test is Passed... ***************")
            self.driver.close()
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_Login.png")
            self.logger.error ("*************** Login Page Title Test is Failed... ***************")
            assert False
            self.driver.close()