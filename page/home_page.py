import allure

from base.base_action import BaseAction
import page

# 包含点击首页 分类 购物车 我的
class HomePage(BaseAction):
    # 初始化方法 动态传递driver
    def __init__(self, driver):
        BaseAction.__init__(self, driver)

    # 点击我的
    @allure.step('点击我的')
    def click_my_btn(self):

        allure.attach('点击我的', '找到 我的 按钮实现点击')
        self.click_element(page.aolai_home_my_btn)



