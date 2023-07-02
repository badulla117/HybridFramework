from selenium.webdriver.common.by import By

class SearchCustomer():

    text_Email_xpath = "//input[@id='SearchEmail']"
    text_FirstName_xpath = "//input[@id='SearchFirstName']"
    text_LastName_xpath = "//input[@id='SearchLastName']"
    button_Search_xpath = "//button[@id='search-customers']"

    table_xpath = "//table[@id='customers-grid']"
    table_Rows_xpath = "//table[@id='customers-grid']//tbody/tr"
    table_Columns_xpath = "//table[@id='customers-grid']//tbody/tr/td"

    def __init__(self, driver):
        self.driver = driver

    def setEmail(self,email):
        self.driver.find_element(By.XPATH, self.text_Email_xpath).clear()
        self.driver.find_element(By.XPATH, self.text_Email_xpath).send_keys(email)

    def setFirstName(self,firstname):
        self.driver.find_element(By.XPATH, self.text_FirstName_xpath).clear()
        self.driver.find_element(By.XPATH, self.text_FirstName_xpath).send_keys(firstname)

    def setLastName(self,lastname):
        self.driver.find_element(By.XPATH, self.text_LastName_xpath).clear()
        self.driver.find_element(By.XPATH, self.text_LastName_xpath).send_keys(lastname)

    def clickSearch(self):
        self.driver.find_element(By.XPATH, self.button_Search_xpath).click()

    def getNoOfRows(self):
        return len(self.driver.find_elements(By.XPATH,self.table_Rows_xpath))

    def getNoOfColumns(self):
        return len(self.driver.find_elements(By.XPATH,self.table_Columns_xpath))

    def searchCustomerByEmail(self,email):
        flag = False
        for r in range(1,self.getNoOfRows()+1):
            table = self.driver.find_element(By.XPATH,self.table_xpath)
            emailid = table.find_element(By.XPATH,"//table[@id='customers-grid']/tbody/tr["+str(r)+"]/td[2]").text
            if emailid == email:
                flag = True
                break
        return flag

    def searchCustomerByName(self,name):
        flag = False
        for r in range(1, self.getNoOfRows() +1):
            table = self.driver.find_element(By.XPATH, self.table_xpath)
            name1 = table.find_element(By.XPATH,"//table[@id='customers-grid']/tbody/tr[" + str (r) + "]/td[3]").text
            if name1 == name :
                flag = True
                break
        return flag