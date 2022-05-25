# 用例当中  每一个步骤 ==== 调页面对象的行为 + 测试数据
#                                                      ||
#                                               页面对象
#                                                     ||
#                                               selenium webdiver  API
#                                               日志/失败 截图     （二次封装）
#                                                     ||
#                                        最常用：1.等待可见
#                                                      2.查找元素
#                                                      3.点击        - 必然的前提：等待和查找
#                                                      4.输入        - 必然的前提：等待和查找
#                                                      5.获取属性     - 必然的前提：等待和查找
#                                                      6.获取文本     - 必然的前提：等待和查找
from time import sleep
import time

from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.common.touch_action import TouchAction
from pywinauto import Desktop
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.remote.webdriver import WebDriver
from appium.webdriver import Remote

from JiaoZiDT_AppClient_PO.Common.dir_config import screenshot_dir
from JiaoZiDT_AppClient_PO.Common.logger import MyLogging
from JiaoZiDT_Web_PO.Common.dir_config import logs_dir

#记住  记录日志/失败截图+错误信息输出 +抛出异常


class BasePage:
    def __init__(self,driver: Remote):
        #初始化 driver
        self.driver=driver
        #初始化log
        self.logger = MyLogging("debug")

    def save_page_shot(self, img_name):
        now = time.strftime("%Y-%m-%d %H_%M_%S")
        screenshot_path = screenshot_dir + "/{}_{}.png".format(img_name, now)
        self.driver.save_screenshot(screenshot_path)
        self.logger.info("截取当前页面图片保存在： {}".format(screenshot_path))

#图片上传
    def upload_photo(self,loc,photo_name,img_name,timeout=20):
        self.wait_element_visible(loc, img_name, timeout)
        self.click_element(loc, img_name, timeout)

        app = Desktop()
        sleep(2)
        # 根据名字找到弹出窗口
        dialog = app["打开"]
        sleep(1)
        dialog["Edit"].type_keys(photo_name)
        sleep(2)
        try:
            dialog["Button"].click()
        except:
            self.save_page_shot(img_name)
            self.logger.exception("图片上传失败！")
            raise

#1.等待元素可见
    def wait_element_visible(self,loc,img_name,timeout=20):
        self.logger.info('等待 {} 元素可见.'.format(loc))

        try:
            WebDriverWait(self.driver,timeout).until(expected_conditions.visibility_of_element_located(loc))
        except:
            #失败截图--写入日志
            self.save_page_shot(img_name)
            self.logger.exception("等待元素可见失败：")
            raise

#等待元素可点击
    def wait_element_clickable(self,loc,img_name,timeout=20):
        try:
            WebDriverWait(self.driver,timeout).until(expected_conditions.element_to_be_clickable(loc))
        except:
            #失败截图--写入日志
            self.save_page_shot(img_name)
            self.logger.exception("等待元素可点击失败：")
            raise

#2.查找元素
    def get_element(self,loc,img_name,timeout=15):
        self.logger.info("在 {} 查找元素：{}.".format(img_name,loc))
        try:
            self.wait_element_visible(loc, img_name, timeout)
            ele=self.driver.find_element(*loc)
        except:
            #截图--日志输出
            self.save_page_shot(img_name)
            self.logger.exception("查找元素失败！")
            return
        return ele

#3.点击元素
    def click_element(self,loc,img_name,timeout=20):
        self.wait_element_visible(loc,img_name,timeout)  #必然的前提
        ele=self.get_element(loc,img_name)#必然的前提
        self.logger.info("在 {} 点击{}元素.".format(img_name, loc))
        try:
            ele.click()
        except:
            self.save_page_shot(img_name)
            self.logger.exception("点击元素失败！")
            raise

#4.元素输入操作
    def input_text(self,loc,value,img_name,timeout=20):
        self.wait_element_visible(loc, img_name, timeout)  # 必然的前提
        ele = self.get_element(loc, img_name) # 必然的前提
        self.logger.info("在 {} 往元素 {} 输入文本值：{}.".format(img_name, loc, value))
        try:
            # phone = self.find_element(MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("搜索商家或商品名称")')
            ele.click()
            sleep(2)
            self.driver.press_keycode(value)
                # .press_keycode(8).press_keycode(84)

            # ele.send_keys(value)
        except:
            self.save_page_shot(img_name)
            self.logger.exception("元素输入文本失败！")
            raise

#5.获取元素属性
    def get_element_attribute(self,loc,attr_name,img_name,timeout=20):
        self.wait_element_visible(loc, img_name, timeout)  # 必然的前提
        ele = self.get_element(loc, img_name)  # 必然的前提
        self.logger.info("在 {} 获取元素 {} 的 {} 属性.".format(img_name, loc, attr_name))
        try:
            value=ele.get_attribute(attr_name)
        except:
            self.save_page_shot(img_name)
            self.logger.exception("获取元素的属性失败！")
            raise
        else:
            self.logger.info("属性值为：{}".format(value))
            return value

#6.获取元素文本
    def get_element_text(self,loc,img_name,timeout=20):
        self.wait_element_visible(loc, img_name, timeout)  # 必然的前提
        ele = self.get_element(loc, img_name)  # 必然的前提
        self.logger.info("在 {} 获取元素 {} 的文本内容.".format(img_name, loc))
        try:
            text = ele.text
        except:
            self.save_page_shot(img_name)
            self.logger.exception("获取元素的文本失败！")
            raise
        else:
            self.logger.info("文本值为：{}".format(text))
            return text



#获取设备大小
#滑屏操作 - 上下左右
#列表滑动 - 找文本/找元素/向上/向下
# toast获取
    def get_toast_msg(self,text,img_name):

        #xpath表达式
        # loc=(MobileBy.XPATH,'//*[contains(@text(),{})]'.format(text))
        print('获取弹窗')
        sleep(1)
        loc=self.driver.find_element(By.XPATH,'//android.widget.Toast')
        self.logger.info("获取toast提示信息，toast元素为：{}".format(loc))
        # 等待元素出现并获取元素内容
        # return self.get_element_text(loc,img_name,10)
        print(loc)

#滑动屏幕
    def slide_the_screen(self,loc,img_name):

        # 1.获取整个屏幕得大小
        size = self.driver.get_window_size()
        # 2.示例化TouchAction类
        tc = TouchAction(self.driver)
        self.logger.info("在 {} 获取元素 {}的文本内容.".format(img_name,loc))
        i = 0
        while i < 10:
            sleep(2)
            try:
                self.driver.find_element(*loc)
            except:
                self.driver.swipe(size["width"] * 0.5, size["height"] * 0.4, size["width"] * 0.5,size["height"] * 0.2, 200)
                sleep(2)
                i = i + 1
            else:
                self.logger.info("{} 元素找到 .".format(loc))
                break


# if __name__ == '__main__':
#     from selenium import webdriver
#     driver = webdriver.Chrome()
#     driver.get("http://www.baidu.com")
#     #调用页面操作行为。 实例化
#     bp=BasePage(driver)
#     sousuo=("id","kw")
#     but=("id","su1")
#     bp.input_text(sousuo,"柠檬班",'百度首页——搜索输入框')
#     bp.click_element(but,"点击-搜索",1)







