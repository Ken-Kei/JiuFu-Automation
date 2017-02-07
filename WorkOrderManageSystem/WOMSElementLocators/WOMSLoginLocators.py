# -*- coding: UTF-8 -*-


"""
Author       :  Ken-Kei
Create Date  :  2016/12/29
"""


from selenium.webdriver.common.by import By


class LoginPageLocators:

    """
    Name         :  登入登出 - 元素定位
    Author       :  Ken-Kei
    Create Date  :  2016/12/29
    """

    USERNAMEINPUTFIELD                      = (By.ID, "username")
    PASSWORDINPUTFIELD                      = (By.ID, "password")
    LOGINBUTTON                             = (By.ID, "loginButton")
    LOGOUTBUTTON                            = (By.XPATH, "html/body/div[1]/div/div[2]/ul/li[3]/a/i")
    LOGOUTCONFIRMBUTTON                           = (By.ID, "isLogoutConfirm")
