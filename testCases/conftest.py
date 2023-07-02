from selenium import webdriver
import pytest

# @pytest.fixture()
# def setup():
#     driver = webdriver.Chrome()
#     driver.maximize_window()
#     driver.implicitly_wait(10)
#     return driver

@pytest.fixture()
def setup(browser):
    if browser == "chrome":
        print("Launching Chrome Browser.......")
        driver = webdriver.Chrome()
    elif browser == "edge":
        print("Launching MicroEdge Browser.......")
        driver = webdriver.Edge()
    elif browser == "firefox":
        print("Launching Mozilla Firefox Browser.......")
        driver = webdriver.Firefox()
    else:
        print("Launching Chrome Browser.......")
        driver = webdriver.Chrome()

    driver.maximize_window()
    driver.implicitly_wait(5)
    return driver

def pytest_addoption(parser): # This will get the value from CLI/hooks
    parser.addoption("--browser")

@pytest.fixture()
def browser(request): # This will return the Browser value to setup method
    return request.config.getoption("--browser")

"""Pytest HTML Reports......."""

#It is hook for Adding Environment info to HTML Report
def pytest_configure(config):
    config._metadata['Project Name'] = 'nop Commerce'
    config._metadata['Module Name'] = 'Customers'
    config._metadata['Tester'] = 'Badulla'

#It is hook for delete/Modify Environment info to HTML Report
@pytest.hookimpl(optionalhook=True)
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME", None)
    metadata.pop("Plugins", None)


# pytest -v -n=2 --html=Reports\report.html testCases/test_Login.py --browser firefox
# pytest -v -n=2 --html=Reports\report.html testCases/test_DDT_Login.py --browser firefox

# pytest -v --html=Reports\report_login_ddt.html testCases/test_DDT_Login.py

#pytest -s -v testCases/test_AddCustomer.py --browser chrome

#pytest -s -v testCases/test_SearchCustomerByEmail.py

#pytest -s -v testCases/test_SearchCustomerByName.py

#pytest -v -m "sanity" --html=Reports\sanity_report.html testCases/ --browser chrome

#java -jar jenkins.war --httpPort=8080