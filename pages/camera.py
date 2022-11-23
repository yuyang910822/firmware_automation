
import time

from base.androir_base_mothod import Android_base
from base.driver import Android_drive


class Camera(Android_base):
    """相机模块"""
    # 辅助驱动器，用于测试过程中对其他设备依赖

    driver_two = Android_base(driver=Android_drive().android_drive)

    def photos(self, number):
        """
        拍照
        :param number: 拍照数量
        :return:
        """
        global n
        self.delete_photos()
        for i in range(1, number+1):
            self.log.info(f'拍照{number}张，当前第{i}张')
            self.input_tap()
            time.sleep(3)

        try:
            n = self.count_photos_number()
            if n == number:
                self.log.info('测试拍照通过')

                return True
            else:
                self.log.error(f'预期拍照{number},实际拍照{n}')
                return False
        except:
            self.log.error('断言失败')
            return False

    def click_photos_info(self):
        """
        检查照片名称格式
        :return:
        """
        try:
            self.photos(1)
            photos_info = self.read_photos_name().split("_")
            if photos_info[0] == 'SV' and photos_info[1] == 'IMG' and photos_info[2] == self.getDate() and self.getTime()-int(photos_info[3]) <=60 and photos_info[-1][-5:].strip('\n') == '.jpg':
                self.log.info(f'测试照片格式通过')
                return True
            else:
                self.log.error(f'照片名称为{photos_info}')
        except:
            self.log.error('断言失败')
            return False

    def click_ratio(self):
        pass
        self.driver.find_element()
