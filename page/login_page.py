import allure

from base.base_action import BaseAction
import page


class LoginPage(BaseAction):

    def __init__(self, driver):
        BaseAction.__init__(self, driver)




    # 输入账号输入密码点击登录
    @allure.step('点击已有账号去登录')
    def click_login_btn(self, username, password):

        # 输入账号
        allure.attach('输入账号', '找到输入框输入')
        self.input_edit_content(page.login_edit_account, username)

        # 输入密码
        allure.attach('输入密码', '找到密码框输入')
        self.input_edit_content(page.login_edit_password, password)

        # 点击登录
        allure.attach('点击登录', '找到登录按钮')
        self.click_element(page.login_btn)

    #3 点击关闭登录页面的功能
    @allure.step('点击关闭登录页面')
    def click_close_login_page(self):
        self.click_element(page.aolai_login_btn_close_login)