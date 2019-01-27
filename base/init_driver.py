from appium import webdriver

# 只要调用这个函数，就能获取一个driver
def init_driver(app_package, app_activity):
    desired_caps = {}
    # 设备信息
    desired_caps['platformName'] = 'Android'
    desired_caps['platformVersion'] = '5.1'
    desired_caps['deviceName'] = 'a'

    # 支持Toast
    desired_caps['automationName'] = 'Uiautomator2'

    # app信息
    desired_caps['appPackage'] = app_package
    desired_caps['appActivity'] = app_activity

    # 支持输入中文
    desired_caps['unicodeKeyboard'] = True
    desired_caps['resetKeyboard'] = True

    return webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)



