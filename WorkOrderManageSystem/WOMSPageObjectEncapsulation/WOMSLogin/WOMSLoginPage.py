
"""
Author       :  Ken-Kei
Create Date  :  2016/12/30
"""

from selenium.common.exceptions import NoSuchElementException
from WorkOrderManageSystem.WOMSElementLocators.WOMSLoginLocators import LoginPageLocators
from BasePage import BasePage
import logging
from LogInfo import *


class LoginPageAction(BasePage):

    """
    Name        :  登入登出
    Author      :  Ken-Kei
    Create Date :  2016/08/23
    """

    def type_username(self, user):
        try:
            self.type(LoginPageLocators.USERNAMEINPUTFIELD, user)
        except NoSuchElementException:
            logging.error(LoginLogInfo.USERNAMEINPUTFIELDNOTFOUND)
        except Exception as e:
            raise e

    def type_password(self, password):
        try:
            self.type(LoginPageLocators.PASSWORDINPUTFIELD, password)
        except NoSuchElementException:
            logging.error(LoginLogInfo.PASSWORDINPUTFIELDNOTFOUND)
        except Exception as e:
            raise e

    def click_login_button(self):
        try:
            self.click(LoginPageLocators.LOGINBUTTON)
        except NoSuchElementException:
            logging.error(LoginLogInfo.LOGINBUTTONNOTFOUND)
        except Exception as e:
            raise e

    # 封装了输入url,输入用户名，输入密码并且点击登录按钮的登入操作
    def login(self, url, user, password):
        self.type_url(url)
        self.type_username(user)
        self.type_password(password)
        self.click_login_button()

    # def click_logout_button(self):
    #     try:
    #         self.click(LoginPageLocators.LOGOUTBUTTON)
    #     except NoSuchElementException:
    #         logging.error(LoginLogInfo.LOGOUTBUTTONNOTFOUND)
    #     except Exception as e:
    #         raise e

    # def logout(self):
    #     self.click_logout_button()
