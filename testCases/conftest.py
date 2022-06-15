from selenium import webdriver
import  pytest

@pytest.fixture()
def setUp():
    driver=webdriver.Chrome(executable_path="D:\selenium_air\Drivers\chromedriver.exe")
    return driver

def pytest_configure(config):
    config._metadata['Project Name'] = 'nop commerce'
    config._metadata['Module Name'] = 'Customers'
    config._metadata['Tester'] = 'Vipin'