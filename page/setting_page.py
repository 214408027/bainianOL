import time

import allure

from base.base_action import BaseAction
import page

# 包含点击首页 分类 购物车 我的
class SettingPage(BaseAction):
    # 初始化方法 动态传递driver
    def __init__(self, driver):
        BaseAction.__init__(self, driver)

    # 退出登录
    @allure.step('退出登录')
    def click_setting_logout(self):

        # 让页面滑动到底部
        allure.attach('滑动', '滑动到底部')
        self.swipe_screen(1)

        time.sleep(1)

        # 点击退出按钮
        allure.attach('点击退出', '点击退出按钮')
        self.click_element(page.setting_logout_btn)

        # 点击弹框的确定按钮
        allure.attach('点击确认', '点击确认按钮')
        self.click_element(page.setting_dialog_confirm)