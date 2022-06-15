import pytest
from selenium import webdriver
from pageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen

class Test_001_Login:
    baseUrl = ReadConfig.getApplicationUrl()
    username = ReadConfig.getUsername()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen()

    def test_HomePageTitle(self,setUp):
        self.logger.info("******************Test_001_Login*****************")
        self.driver = setUp
        self.driver.get(self.baseUrl)
        act_title=self.driver.title
        if act_title=="Your store. Login 123":
            assert True
            self.driver.close()
            self.logger.info("******************Test_001_Login close*****************")
        else:

            self.driver.save_screenshot(".\\Screenshots\\" + "test_HomePageTitle.png")
            self.logger.error("******************Test_001_Login error*****************")
            self.driver.close()
            assert False


    def test_Login(self,setUp):
        self.logger.info("******************Test_002_Login*****************")
        self.driver = setUp
        self.driver.get(self.baseUrl)
        self.lp=LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        act_title=self.driver.title
        if act_title=="Dashboard / nopCommerce administration":
            assert True
            self.driver.close()
        else:

            self.driver.save_screenshot(".\\Screenshots\\" + "test_Login.png")
            self.driver.close()
            assert False
