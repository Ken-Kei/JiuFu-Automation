# -*- coding: UTF-8 -*-


"""
Author       :  Ken-Kei
Create Date  :  2016/07/01
"""


import configparser
import time
import os


# ====================================================================
config = configparser.ConfigParser()
config.read("E:\PythonWorkspace\Automation\JiuFu-Automation\config.ini")
# ====================================================================


# ====================================================================
"""指定驱动文件位置"""
ie_driver_path = os.path.join("./Driver/IEDriverServer.exe")
# ====================================================================


# ====================================================================
"""Config.ini属性配置"""

# [url_info]
browser = config.get("url_info", "browser")  # 选择浏览器
main_url = config.get("url_info", "main_url")  # 主页url
waiting_time = config.getint("url_info", "waiting_time")  # 页面等待时间
operation_system = config.get("url_info", "operation_system")  # 测试使用的操作系统

# [driver_path_info]
chrome_driver_path = config.get("driver_path_info", "chrome_driver_path")  # chrome driver文件路径

# [account_info]
account_row = config.getint("account_info", "account_row")  # 读取到excel表的账号行数
username = config.get("account_info", "username")  # 后台使用的账号
password = config.get("account_info", "password")  # 后台使用的密码
wrong_username = config.get("account_info", "wrong_username")  # 错误的用户名
wrong_password = config.get("account_info", "wrong_password")  # 错误的密码

# [test_result]
data_source = config.get("test_result", "data_source")  # 测试数据数据源
need_screenshot = config.get("test_result", "need_screenshot")  # 是否需要截图

# [email_info]
smtp_server = config.get("email_info", "smtp_server")  # smtp服务器地址
smtp_server_port = config.get("email_info", "smtp_server_port")  # smtp服务器地址端口号
from_email_address = config.get("email_info", "from_email_address")  # 发件人账号
from_email_address_pwd = config.get("email_info", "from_email_address_pwd")  # 发件人密码
to_mail_address = config.get("email_info", "to_email_address").split(',')  # 收件人地址
cc_mail_address = config.get("email_info", "cc_email_address").split(',')  # 抄送人地址

# [cron_job_time_setting]
time_set = config.get("cron_job_time_setting", "time_set")  # 定时任务触发的时间
# ====================================================================


# ====================================================================
# """初始化读excel操作"""
#
# data_source_path = os.path.join("./DataSource/" + data_source)
# data = xlrd.open_workbook(data_source_path)
# table = data.sheet_by_name('account')
# copy_data = copy(data)
# copy_sheet = copy_data.get_sheet(0)
# ====================================================================


# ====================================================================
"""log文件和截图文件路径变量"""

launch_log_path = os.path.join("./Log/Log_" + time.strftime("%Y%m%d"))
launch_screenshot_path = os.path.join("./Log/Screenshot_" + time.strftime("%Y%m%d") + "/" + time.strftime("%H%M%S"))
launch_result_path = os.path.join("./Result/Result_" + time.strftime("%Y%m%d"))
# ====================================================================


# ====================================================================
"""截图文件名"""

# 登入登出截图
login_failed_screenshot = '登录失败'
login_succeed_screenshot = '登录成功'
logout_succeed_screenshot = '登出成功'
logout_failed_screenshot = '登出失败'

# 创建套图分类
create_pc_succeed_screenshot = '创建套图分类成功'
create_pc_failed_screenshot = '创建套图分类失败'

# 创建套图
create_pk_succeed_screenshot = '创建套图成功'
create_pk_failed_screenshot = '创建套图失败'

# 创建卡券
create_card_succeed_screenshot = '创建卡券成功'
create_card_failed_screenshot = '创建卡券失败'
card_name_exist_screenshot = '创建卡券失败-卡券名称重复'

# 创建微助力活动
create_mh_succeed_screenshot = '创建微助力成功'
create_mh_failed_screenshot = '创建微助力失败'

# 创建渠道二维码
create_code_succeed_screenshot = '创建渠道二维码成功'
create_code_failed_screenshot = '创建渠道二维码失败'
# ====================================================================


# 图库上传的元素位置
# .//*[@id='upImgs']/div/div/div[4]/div/div[2]/div/div[1]/div


# ====================================================================
"""用例名"""

test_LoginSucceed = '登入以及登出工单系统成功'
test_LoginFailedWithWrongUser = '错误的用户名登录'
test_LoginFailedWithWrongPwd = '错误的密码登录'
test_CreatePictureClassify = '创建套图分类'
test_CreatePictureKit = '创建套图'
test_CreateCard = '创建卡券'
test_CreateMicroHelp = '创建微助力活动'
test_CreateQRCode = '创建渠道二维码'
# ====================================================================


# ====================================================================
"""log信息"""

loging_in = "正在使用此用户登录: %s"
# ====================================================================


# ====================================================================
"""指定邮件标题、正文及其它信息"""

# 邮件标题
subject = '自动化用例执行结果'

# 邮件正文
main_body = """
自动化测试用例已经执行完成，以下为测试报告概况，用例的详细执行状况请查看附件。

==============================================


这是自动发送的邮件，请勿答复。



以上
测试组
"""
# ====================================================================


# ====================================================================
"""JS语句"""

# 上传图片的元素id为fileImage
file_image_block = """document.getElementById('fileImage').style.display='block'; """
file_image_none = """document.getElementById('fileImage').style.display='none'; """
remove_sd_read_only = """document.getElementById('js-startDate').readOnly=false; """
remove_ed_read_only = """document.getElementById('js-endDate').readOnly=false; """
# ====================================================================
