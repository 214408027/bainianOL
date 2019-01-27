import os,sys
sys.path.append(os.getcwd())


import time

import pytest
from base.init_driver import init_driver
from page.navigation_page import NavigationPage
import page
from base.read_yaml import read_yaml_data


# 读取yaml数据


def get_login_data():
    login_data_list = []
    login_data = read_yaml_data("login_data.yaml")
    for i in login_data.keys():
        username = login_data.get(i).get('username')
        password = login_data.get(i).get('password')
        tag = login_data.get(i).get('tag')
        expect_data = login_data.get(i).get('expect_data')
        login_data_list.append((username, password, tag, expect_data))
        # print(login_data_list)
    return login_data_list

# get_login_data()
# print(login_data_list)


class TestLogin:

    def setup_class(self):
        # 初始化driver
        self.driver = init_driver(page.aolai_app_package, page.aolai_app_activity)
         # 实例类
        self.navigation_page = NavigationPage(self.driver)
        # self.driver.implicitly_wait(10)

    def teardown_class(self):
        time.sleep(1)
        self.driver.quit()

    @pytest.mark.parametrize("username, password, tag, expect_data", get_login_data())
    def test_login(self, username, password, tag, expect_data):
        time.sleep(2)
        # 点击我的
        self.navigation_page.get_home_page_obj().click_my_btn()
        time.sleep(1)

        # 点击已有账号去登录
        self.navigation_page.get_regist_obj().click_btn_already_account()
        time.sleep(1)

        # 输入账号密码登录
        self.navigation_page.get_login_page_obj().click_login_btn(username, password)
        time.sleep(1)

        if tag == 1:

            try:
                # 点击个人中心左上角的设置按钮
                time.sleep(2)
                self.navigation_page.get_person_center_obj().click_letf_setting_btn()

                # 实现滑动,点击退出 点击确认
                self.navigation_page.get_setting_obj().click_setting_logout()

            except Exception:
                # 出现异常的情况，截图
                self.navigation_page.get_setting_obj().get_screen()
                time.sleep(1)

        else:

            # 获取toast
            toast_msg = self.navigation_page.get_login_page_obj().find_element(page.pwd_error_toast).text
            time.sleep(2)
            print(toast_msg)
            assert toast_msg == expect_data, self.navigation_page.get_setting_obj().get_screen()
            self.navigation_page.get_login_page_obj().click_close_login_page()
