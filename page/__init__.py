from selenium.webdriver.common.by import By

# 百年奥莱包名和启动名
aolai_app_package = 'com.yunmall.lc'
aolai_app_activity = 'com.yunmall.ymctoc.ui.activity.MainActivity'


# 页面定位

# home页面
# 定位 我的
aolai_home_my_btn = By.ID, 'com.yunmall.lc:id/tab_me'
# 定位到购物车
aolai_home_shopping_cart = By.ID, 'com.yunmall.lc:id/tab_shopping_cart'


# 注册页面
# 定位到 已有账号去登录
regist_btn_already_account = By.ID, 'com.yunmall.lc:id/textView1'


# 登录页面
# 定位到账号
login_edit_account = By.ID, 'com.yunmall.lc:id/logon_account_textview'
# 定位到密码
login_edit_password = By.ID, 'com.yunmall.lc:id/logon_password_textview'
# 登录按钮
login_btn = By.ID, 'com.yunmall.lc:id/logon_button'

#3.4 定位到关闭按钮
aolai_login_btn_close_login= By.ID,"com.yunmall.lc:id/ymtitlebar_left_btn_image"


# 账号密码
# 13488834010
# 159357li


# 个人中心页面
# 定位到左上角设置按钮
person_center_btn_left_setting = By.ID, 'com.yunmall.lc:id/ymtitlebar_left_btn_image'


# 设置页面
# 退出按钮
setting_logout_btn = By.XPATH, '//*[contains(@text, "退出")]'
# 弹框确认按钮
setting_dialog_confirm = By.ID, 'com.yunmall.lc:id/ymdialog_right_button'


# 定位toast
pwd_error_toast = By.XPATH,"//*[contains(@text,'登录密码错误')]"