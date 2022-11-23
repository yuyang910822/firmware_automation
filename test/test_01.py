import unittest

from base.driver_setart import Driver_Session
from page.camera import Camera


class Test_Camers(Driver_Session):
    """拍照模块"""

    def test01(self):
        """拍照"""
        c = Camera(self.driver)
        self.assertTrue(c.photos(10), True)

    def test02(self):
        """检查照片存储格式"""

        c = Camera(self.driver)
        self.assertTrue(c.click_photos_info(), True)
