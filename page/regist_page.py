import allure

from base.base_action import BaseAction
import page

class RegistPage(BaseAction):

    def __init__(self, driver):
        BaseAction.__init__(self, driver)


    # 点击已有账号去登录
    @allure.step('点击已有账号去登录')
    def click_btn_already_account(self):

        allure.attach('点击已有账号', '找到已有账号去登录')
        self.click_element(page.regist_btn_already_account)

