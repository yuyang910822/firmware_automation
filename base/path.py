import os

# 项目根目录
dir_path = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))

# appium参数配置文件路径
appium_yaml_path = os.path.join(dir_path, r'data\appium_config.yaml')

# 失败用例截图存储目录
img_path = os.path.join(dir_path, r'reports\images')

# 日志存储目录
log_dir = os.path.join(dir_path, r'../log\camera.log')

# 测试用例存储目录
test_dir = os.path.join(dir_path, r'../test')

# 测试报告存储目录
report_dir = os.path.join(dir_path, r'reports')

# 测试报告截图目录
png_dir = os.path.join(dir_path, r'png')
