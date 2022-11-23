import time
import unittest
import warnings

from appium import webdriver
from base.path import *
from config.read_yaml import read_yaml


class Firmware_drive(unittest.TestCase):
    """驱动会话"""


    appium_config = read_yaml(appium_yaml_path)['svg1']['desired_caps']
    server = 'http://127.0.0.1:4723/wd/hub'
    desired_caps = {"deviceName": appium_config['deviceName'],
                    "automationName": appium_config["automationName"],
                    "platformName": appium_config["platformName"],
                    "autoAcceptAlerts": appium_config["autoAcceptAlerts"],
                    "noReset": appium_config["noReset"],
                    "appPackage": appium_config["appPackage"],
                    "appActivity": appium_config["appActivity"],
                    "newCommandTimeout": appium_config["newCommandTimeout"]
                    }

    @classmethod
    def setUpClass(cls) -> None:
        """前置"""
        os.system('chcp 65001 ')
        os.system('adb shell dumpsys battery set usb 0')
        cls.firmware_drive = webdriver.Remote(cls.server, cls.desired_caps)
        warnings.simplefilter('ignore', ResourceWarning)
        print('启动')
        time.sleep(5)

    @classmethod
    def tearDownClass(cls) -> None:
        """后置"""
        print('退出')
        os.system('adb shell dumpsys battery set usb 1')
        cls.firmware_drive.quit()


class Android_drive():
    """驱动会话"""


    appium_config = read_yaml(appium_yaml_path)['svg1']['desired_caps']
    server = 'http://127.0.0.1:4723/wd/hub'
    desired_caps = {"deviceName": appium_config['deviceName'],
                    "automationName": appium_config["automationName"],
                    "platformName": appium_config["platformName"],
                    "autoAcceptAlerts": appium_config["autoAcceptAlerts"],
                    "noReset": appium_config["noReset"],
                    "appPackage": appium_config["appPackage"],
                    "appActivity": appium_config["appActivity"],
                    "newCommandTimeout": appium_config["newCommandTimeout"]
                    }

    @classmethod
    def setUpClass(cls) -> None:
        """前置"""
        os.system('chcp 65001 ')
        os.system('adb shell dumpsys battery set usb 0')
        cls.android_drive = webdriver.Remote(cls.server, cls.desired_caps)
        warnings.simplefilter('ignore', ResourceWarning)
        print('启动')
        time.sleep(5)

    @classmethod
    def tearDownClass(cls) -> None:
        """后置"""
        print('退出')
        os.system('adb shell dumpsys battery set usb 1')
        cls.android_drive.quit()