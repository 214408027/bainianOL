import allure

from base.base_action import BaseAction
import page

# 包含点击首页 分类 购物车 我的
class PersonCenterPage(BaseAction):
    # 初始化方法 动态传递driver
    def __init__(self, driver):
        BaseAction.__init__(self, driver)

    # 点击左上角设置按钮
    @allure.step('点击左上角设置按钮')
    def click_letf_setting_btn(self):
        self.click_element(page.person_center_btn_left_setting)