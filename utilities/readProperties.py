import configparser

config=configparser.RawConfigParser()
config.read(".\\Configurations\\config.ini")

class ReadConfig():
    @staticmethod
    def getApplicationUrl():
        url=config.get('comman info','baseUrl')
        return url

    @staticmethod
    def getUsername():
        username=config.get('comman info','username')
        return username

    @staticmethod
    def getPassword():
        password=config.get('comman info','password')
        return password
