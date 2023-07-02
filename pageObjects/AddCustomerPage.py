import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

class AddCustomer():
    """
    All Elements Locators
    """

    link_CustomersMenu_xpath = "//a[@href='#']//p[contains(text(),'Customers')]"
    link_CustomersMenuList_xpath = "//a[@href='/Admin/Customer/List']//p[contains(text(),'Customers')]"
    button_Addnew_xpath = "//a[@href='/Admin/Customer/Create']"

    text_UserEmail_xpath = "//input[@name='Email']"
    text_UserPassword_xpath = "//input[@name='Password']"
    text_UserFirstName_xpath = "//input[@name='FirstName']"
    text_UserLastName_xpath = "//input[@name='LastName']"

    radiobutton_MaleGender_xpath = "//input[@value='M']"
    radiobutton_FemaleGender_xpath = "//input[@value='F']"

    text_DateofBirth_xpath = "//input[@name='DateOfBirth']"
    text_CompanyName_xpath = "//input[@name='Company']"

    checkbox_Tax_xpath = "//input[@id='IsTaxExempt']"

    text_Newsletter_xpath = "//div[@class='input-group-append']//div[@role='listbox']"
    listItem_YourStoreName_xpath = "//li[contains(text(),'Your store name')]"
    listItem_TestStore_xpath = "//li[contains(text(),'Test store 2')]"

    text_CustomerRoles_xpath = "//select[@id='SelectedCustomerRoleIds']/.."
    listItem_Administractor_xpath = "//li[text()='Administrators']"
    listItem_Forum_xpath = "//li[text()='Forum Moderators']"
    listItem_Guests_xpath = "//li[text()='Guests']"
    listItem_Registered_xpath = "//li[text()='Registered']"
    listItem_Vendors_xpath = "//li[text()='Vendors']"

    dropdown_Vendor_xpath = "//select[@id='VendorId']"
    text_AdminComment_xpath = "//textarea[@id='AdminComment']"

    button_Save_xpath = "//button[@name='save']"

    popup_Message_tagname = "body"

    def __init__(self,driver):
        self.driver = driver

    def clickOnCustomersMenu(self):
        self.driver.find_element(By.XPATH,self.link_CustomersMenu_xpath).click()

    def clickOnCustomersMenuItem(self):
        self.driver.find_element(By.XPATH,self.link_CustomersMenuList_xpath).click()

    def clickOnAddNewButton(self):
        self.driver.find_element(By.XPATH,self.button_Addnew_xpath).click()

    def setEmail(self,email):
        self.driver.find_element(By.XPATH,self.text_UserEmail_xpath).send_keys(email)

    def setPassword(self,password):
        self.driver.find_element(By.XPATH,self.text_UserPassword_xpath).send_keys(password)

    def setFirstName(self,firstname):
        self.driver.find_element(By.XPATH,self.text_UserFirstName_xpath).send_keys(firstname)

    def setLastName(self,lastname):
        self.driver.find_element(By.XPATH,self.text_UserLastName_xpath).send_keys(lastname)

    def setGender(self,gender):
        if gender == "Male":
            self.driver.find_element(By.XPATH,self.radiobutton_MaleGender_xpath).click()
        elif gender == "Female":
            self.driver.find_element(By.XPATH,self.radiobutton_FemaleGender_xpath).click()
        else:
            self.driver.find_element(By.XPATH,self.radiobutton_MaleGender_xpath).click()

    def setDateOfBirth(self,dateofbirth):
        self.driver.find_element(By.XPATH,self.text_DateofBirth_xpath).send_keys(dateofbirth)

    def setCompanyName(self,companyname):
        self.driver.find_element(By.XPATH,self.text_CompanyName_xpath).send_keys(companyname)

    def selectTax(self):
        self.driver.find_element(By.XPATH,self.checkbox_Tax_xpath).click()

    def setNewLetter(self,news):
        self.driver.find_element(By.XPATH,self.text_Newsletter_xpath).click()
        if news == "Your store name":
            self.driver.find_element(By.XPATH,self.listItem_YourStoreName_xpath).click()
        else:
            self.driver.find_element(By.XPATH,self.listItem_TestStore_xpath).click()

    def setCustomerRoles(self,role):
        self.driver.find_element(By.XPATH, "//ul[@id='SelectedCustomerRoleIds_taglist']//li//span[2]").click()
        # self.driver.find_element(By.XPATH,self.text_CustomerRoles_xpath).click()
        if role == "Administractor":
            self.listItem = self.driver.find_element(By.XPATH,self.listItem_Administractor_xpath)
        elif role == "Forum Moderators":
            self.listItem = self.driver.find_element(By.XPATH,self.listItem_Forum_xpath)
        elif role == "Guests":
            self.listItem = self.driver.find_element(By.XPATH,self.listItem_Guests_xpath)
        elif role == "Registered":
            self.listItem = self.driver.find_element(By.XPATH,self.listItem_Registered_xpath)
        elif role == "Vendors":
            self.listItem = self.driver.find_element(By.XPATH,self.listItem_Vendors_xpath)
        else:
            self.listItem = self.driver.find_element(By.XPATH,self.listItem_Guests_xpath)

        #self.listItem.click()
        self.driver.execute_script("arguments[0].click();",self.listItem)

    def setManagerOfVendor(self,value):
        dropdown = Select(self.driver.find_element(By.XPATH,self.dropdown_Vendor_xpath))
        dropdown.select_by_visible_text(value)

    def setAdminComment(self,comment):
        self.driver.find_element(By.XPATH,self.text_AdminComment_xpath).send_keys(comment)

    def clickSave(self):
        self.driver.find_element(By.XPATH,self.button_Save_xpath).click()