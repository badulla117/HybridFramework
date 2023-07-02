import time

import pytest
from pageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig as config
from utilities.customLogger import Logs
from utilities import ExcelUtility as utility

class Test_002_DDT_Login:
    baseURL = config.getApplicationURL()
    path = ".\\TestData\\Data.xlsx"
    logger = Logs.getLogs()

    @pytest.mark.regression
    def test_DDT_Login(self,setup):
        self.logger.info("*************** Test_002_DDT_Login ***************")
        self.logger.info("*************** Verifying DDT Login Test ***************")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.login = LoginPage(self.driver)

        self.rows = utility.getRowCount(self.path, "Sheet1")
        print("Number of Rows in a Excel Sheet: ", self.rows)

        list_status = [] #Empty List Variable

        for r in range(2, self.rows+1):
            self.username = utility.readData(self.path,"Sheet1",r,1)
            self.password = utility.readData(self.path,"Sheet1",r,2)
            self.exp_res = utility.readData(self.path,"Sheet1",r,3)

            self.login.setUserName(self.username)
            self.login.setPassword(self.password)
            self.login.clickLogin()
            time.sleep(5)

            act_title = self.driver.title
            exp_title = "Dashboard / nopCommerce administration"

            if act_title == exp_title:
                if self.exp_res == "Pass":
                    self.logger.info("********* Passed *********")
                    self.login.clickLogout()
                    list_status.append("Pass")
                elif self.exp_res == "Fail":
                    self.logger.error("********* Failed *********")
                    self.login.clickLogout()
                    list_status.append("Fail")
            elif act_title != exp_title:
                if self.exp_res == "Fail":
                    self.logger.info("********* Passed *********")
                    list_status.append("Pass")
                elif self.exp_res == "Pass":
                    self.logger.error("********* Failed *********")
                    list_status.append("Fail")

        if "Fail" not in list_status:
            self.logger.info("********** Login DDT Test Passed.... ***********")
            self.driver.close()
            assert True
        else:
            self.logger.error("********** Login DDT Test Failed...... *********")
            self.driver.close()
            assert False

        self.logger.info("******** End of DDT Login Test... ********")
        self.logger.info("******** __Completed TC_002_DDT_Login__ ********")