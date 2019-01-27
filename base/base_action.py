import time

#包含公共的操作 ：查找元素，点击元素，输入内容...
from selenium.webdriver.support.wait import WebDriverWait


class BaseAction:
    def __init__(self, driver):
        self.driver = driver

    # 查找一个元素
    def find_element(self, loc):
        return self.driver.find_element(loc[0], loc[1])
        # return WebDriverWait(self.driver).until(lambda x:x.find_element(loc[0], loc[1]),10,1)

    # 点击元素的方法
    def click_element(self, loc):
        # 强制等待1秒
        time.sleep(1)
        self.find_element(loc).click()


    # 向输入框里面输入内容
    def input_edit_content(self, loc, content):
        input_element = self.find_element(loc)
        input_element.clear()
        input_element.send_keys(content)


    # 查找一组元素
    def find_elements(self, loc):
        return self.driver.find_elements(loc[0], loc[1])


    # 滑动操作
    # 1 向上滑动 2向下滑动 3向左滑动 4向右滑动
    # tag 1 2 3 4
    def swipe_screen(self,tag):
        time.sleep(1)
        # 获取当前手机窗口的大小
        screen_size = self.driver.get_window_size()
        width = screen_size.get("width")  # 获取手机宽
        height = screen_size.get("height")  # 获取手机的高
        if tag == 1:  # 向上滚动 两点之间滑动  x轴不变
            self.driver.swipe(width * 0.5, height * 0.8, width * 0.5, height * 0.3, 1000)
        if tag == 2:  # 向下滚动
            self.driver.swipe(width * 0.5, height * 0.3, width * 0.5, height * 0.8, 1000)
        if tag == 3:  # 向左滚动
            self.driver.swipe(width * 0.8, height * 0.5, width * 0.3, height * 0.5, 1000)
        if tag == 4:  # 向右滚动
            self.driver.swipe(width * 0.3, height * 0.5, width * 0.8, height * 0.5, 1000)

    # 获取截图
    def get_screen(self):
#         png_name = './screen/{}.png'.format(time.strftime('%Y%m%d%H%M%S'))
#         self.driver.get_screenshot_as_file(png_name)
        png_name = "./screen/{}.png".format(int(time.time()))
        self.driver.get_screenshot_as_file(png_name)
        # rb 以二进制的方式读取数据
        with open(png_name, 'rb') as f:
            allure.attach('截图名字', f.read(), allure.attach_type.PNG)
