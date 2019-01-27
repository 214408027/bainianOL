# from base.base_action import BaseAction
from page.home_page import HomePage
from page.login_page import LoginPage
from page.person_center_page import PersonCenterPage
from page.regist_page import RegistPage
from page.setting_page import SettingPage


# 导航类，负责初始化其他几个类的实例
# 只要获取导航类的实例，就可以获取其他几个类的实例

class NavigationPage:
    def __init__(self, driver):
        # BaseAction.__init__(self, driver)
        self.driver = driver

    # 获取home_page的实例
    def get_home_page_obj(self):
        return HomePage(self.driver)

    # 获取登录页面实例
    def get_login_page_obj(self):
        return LoginPage(self.driver)

    # 获取个人中心实例
    def get_person_center_obj(self):
        return PersonCenterPage(self.driver)

    # 获取注册页面实例
    def get_regist_obj(self):
        return RegistPage(self.driver)

    # 获取设置页面实例
    def get_setting_obj(self):
        return SettingPage(self.driver)
