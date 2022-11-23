# -*- coding: utf-8 -*-
# @Time : 2022/3/16 19:39
# @Author : Yu yang
# @File : log.py

# -*- coding: utf-8 -*-

import logging
from logging.handlers import TimedRotatingFileHandler


class Log(logging.Logger):
    """
    日志收集器
    """

    def __init__(self, name='youran', level='DEBUG', file=None):
        super().__init__(name=name, level=level)
        # 日志格式
        fmt = logging.Formatter("%(levelname)s - %(asctime)s - %(filename)s[line:%(lineno)d] : %(message)s")
        # 日志处理器
        p = logging.StreamHandler()
        p.setLevel('DEBUG')
        p.setFormatter(fmt)
        self.addHandler(p)

        # 文件处理器
        if file:
            f = TimedRotatingFileHandler(file, when='D', backupCount=7, encoding='utf-8')
            f.setLevel('DEBUG')
            f.setFormatter(fmt)
            self.addHandler(f)


if __name__ == '__main__':
    pass