import os
import time

from appium.webdriver.common.touch_action import TouchAction
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver import ActionChains
from base.path import *
from appium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from base.logger_handler import Log


class Android_base:
    """
    安卓基础类：
    1.定义常见定位方法
    2.定义系统常用方法
    """
    def __init__(self, driver: webdriver.Remote):
        """
        初始化方法
        :param driver: 操作目标驱动器
        :param log_file: 记录日志文件地址
        """

        self.driver = driver
        # 全局等待
        self.driver.implicitly_wait(30)
        # 获取屏幕尺寸进行滑动操作
        self.size = self.driver.get_window_size()
        # 日志记录
        self.log = Log(file='log_path')
        # 非全局等待
        self.wait = WebDriverWait(self.driver, 10, 1)

    def visible(self, loc):
        """
        非隐藏元素可见
        :param loc: 定位表达式
        :return:
        """
        self.wait.until(expected_conditions.visibility_of_element_located(loc))

    def presence(self, loc):
        """
        元素加载到DOM树中，不考虑是否可见
        用于判断是否到达或离开指定page
        :return:
        """

    def click(self, loc):
        """
        等待元素可点击下点击元素
        :param loc: 定位表达式
        :return:
        """

        self.wait.until(expected_conditions.element_to_be_clickable(loc))
        self.driver.find_element(*loc)

    def get_text(self, loc):
        """
        等待元素可见获取文本
        :param loc: 定位表达式
        :return: 返回定位元素的文本
        """
        self.visible(loc)
        return self.driver.find_element(*loc).set_text()

    def double_click(self, loc):
        """
        双击
        :param loc: 定位表达式
        :return:
        """
        el = self.driver.find_element(*loc)
        action = ActionChains(self.driver)
        action.double_click(el).perform()

    def screenshot(self):
        """
        截取图片,并保存在images文件夹
        :return:
        """
        HMS = time.strftime('%H%M%S')
        Ymd = time.strftime('%Y%m%d')

        path = os.path.join(img_path, Ymd)
        if not os.path.exists(path):
            os.mkdir(path)
        imgPath = os.path.join(path, r'%s.png' % str(HMS))
        self.driver.save_screenshot(imgPath)
        self.log.debug('screenshot:', f"{HMS}.png")

    def swipe_up(self, x=500, y=2000, x1=500, y1=180):
        """上滑"""
        TouchAction(self.driver).press(x=x, y=y).move_to(x=x1, y=y1).release().perform()

    def swipe_left(self, x=970, y=570, x1=50, y1=570):
        """左滑"""
        TouchAction(self.driver).press(x=x, y=y).move_to(x=x1, y=y1).release().perform()

    def input_tap(self, x=330, y=220):
        """adb 点击"""
        os.system(f'adb shell input tap {x} {y}')

    def count_photos_number(self):
        """
        统计照片数量
        :return: 照片数量
        """
        info = os.popen('adb shell ls sdcard/DCIM/.thumbnails ')

        return len(info.readlines())

    def delete_photos(self):
        """
        删除照片
        :return:
        """
        os.system('adb shell  rm -rf sdcard/DCIM/.thumbnails ')

    def read_photos_name(self):
        """
        获取照片名字
        :return:
        """
        name = os.popen('adb shell ls sdcard/DCIM/.thumbnails').readlines()
        return name[0]

    def getDate(self):
        """
        获取日期
        :return:
        """
        return time.strftime("%Y%m%d")

    def getDateTime(self):
        """
        获取日期时间
        :return:
        """
        return time.strftime("%Y-%m-%d|%H:%M:%S")

    def getTime(self):
        """
        获取时间
        :return:
        """
        return int(time.strftime("%H"))

    def getTimeStamp(self) -> int:
        """时间戳"""
        t = int(time.time() * 1000)
        return t

    def mktimes(self, st):
        """
        日期时间转换时间戳
        :param st 日期时间
        :return:
        """
        dt = time.strptime(st, "%Y-%m-%d %H:%M:%S")
        t = time.mktime(dt)
        return t