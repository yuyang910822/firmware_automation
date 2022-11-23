import unittest

from base.driver import Firmware_drive,Android_drive
from pages.camera import Camera


class Test_Camers(Firmware_drive):
    """拍照模块"""

    def test01(self):
        """拍照"""
        c = Camera(driver=self.firmware_drive)
        self.assertTrue(c.photos(10), True)

    def test02(self):
        """检查照片存储格式"""

        c = Camera(self.firmware_drive)
        self.assertTrue(c.click_photos_info(), True)
