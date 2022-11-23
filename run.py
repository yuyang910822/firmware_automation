# -*- coding: utf-8 -*-
# @Time : 2022/3/16 20:08
# @Author : Yu yang
# @File : run.py

# -*- coding: utf-8 -*-

import os
import smtplib
import unittest
import HTMLTestRunner
import time

from email.mime.image import MIMEImage
from email.mime.application import MIMEApplication
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from selenium.webdriver.common.by import By
from base.path import report_dir, dir_path, png_dir
from selenium import webdriver
from base.path import test_dir


def run():
    # 存放报告的文件夹
    discover = unittest.defaultTestLoader.discover(test_dir, pattern="test*.py", top_level_dir=None)

    # 报告命名时间格式化
    now = time.strftime("%Y%m%d%H%M%S")

    # 报告文件完整路径
    global report_name
    report_name = report_dir + '/' + now + 'result.html'
    print(report_name)
    with open(report_name, 'wb') as f:
        runner = HTMLTestRunner.HTMLTestRunner(stream=f, title=' 测试结果如下：', description='用例执行情况：', verbosity=2)
        # 执行测试用例文件
        runner.run(discover)


def html_png():
    """截图"""
    target_dir = os.path.join(report_dir, os.listdir(report_dir)[-2])
    url = 'http://localhost:63342/{}/reports/{}'.format(
        dir_path.split('\\')[-1],
        target_dir.split('\\')[-1]
    )
    d = webdriver.Chrome()
    d.get(url)
    d.maximize_window()
    d.find_element(By.XPATH, '//*[@class="btn btn-primary"]').click()
    path = os.path.join(png_dir, '1.png')
    d.save_screenshot(path)
    d.quit()
    return path


def runEmail():
    """
    Email发送
    :return:
    """
    run()

    # HTML报告路径
    target_dir = os.path.join(report_dir, os.listdir(report_dir)[-2])

    # 构造邮件主体
    mail_server = "smtp.feishu.cn"
    sender = 'yase@superhexa.com'
    sender_password = 'OXanZZGkSiUOGQ8h'
    receiver = 'yase@superhexa.com'  # 收件人，多个收件人用逗号隔开

    title = ''.join(['【固件', str(time.strftime('%Y.%m.%d.%H.%M.%S', time.localtime(time.time())))]) + "】--测试报告"
    mail = MIMEMultipart()
    mail['Subject'] = title
    mail['From'] = sender  # 发件人
    mail['To'] = receiver  # 收件人；[]里的三个是固定写法，别问为什么，我只是代码的搬运工

    # 构造HTML和图片文本
    msgAlternative = MIMEMultipart('alternative')
    mail.attach(msgAlternative)
    mail_msg = """
    <p>自动化测试已完成，详见附件下载测试报告</p>
    <p><img src="cid:image1"></p>
    """
    msgAlternative.attach(MIMEText(mail_msg, 'html', 'utf-8'))
    fp = open(html_png(), 'rb')
    msgImage = MIMEImage(fp.read())
    fp.close()
    # 定义图片 ID，在 HTML 文本中引用
    msgImage.add_header('Content-ID', '<image1>')

    # 构造附件
    html = MIMEApplication(open(target_dir, 'rb').read())
    html.add_header('Content-Disposition', 'attachment', filename='测试报告.html')

    mail.attach(msgImage)
    mail.attach(html)
    try:
        smtp = smtplib.SMTP(mail_server, port=25)  # 连接邮箱服务器
        smtp.starttls()
        smtp.login(sender, sender_password)  # 登录邮箱
        smtp.sendmail(sender, receiver.split(','), mail.as_string())  # 参数分别是发送者，接收者，第三个是把上面的发送邮件的内容变成字符串
        smtp.quit()  # 发送完毕后退出smtp
    except:
        raise
    else:
        print('success')


if __name__ == '__main__':
    run()
