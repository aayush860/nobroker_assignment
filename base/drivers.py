from appium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


class configure_dirvers:
    def config_driver(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        #desired_caps['platformVersion'] = '10.0'
        desired_caps['deviceName'] = 'Nokia 5'
        #desired_caps['udid'] = 'D1AGAD57B1003790'
        desired_caps['automationName'] = 'UiAutomator1'
        desired_caps['appPackage'] = 'com.nobroker.app'
        desired_caps['appActivity'] = 'com.nobroker.app.activities.NBSplashScreen'
        # capabilities.setCapability("fullReset", "false")
        desired_caps['app'] = '/Users/aayushbhargava/Downloads/nbk.apk'
        driver = webdriver.Remote('http://0.0.0.0:4723/wd/hub', desired_caps)
        driver.implicitly_wait(60)
        return driver

