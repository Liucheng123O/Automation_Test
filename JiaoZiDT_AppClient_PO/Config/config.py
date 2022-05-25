from time import sleep
from appium import webdriver
from selenium.webdriver.support import expected_conditions as EC
       #运行平台
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.wait import WebDriverWait
def init_driver():
    caps={"platformName":"Android",
      #设备端口号
      "deviceName":"f45c94ab",
      #安卓系统版本
      # "platformVersion":"4.3",
      #app重启后，数据不会重置
      "noReset":True,
      #自动化测试名称
      "automationName":"UiAutomator2",
      #app安装地址
      # "app":r"D:\BaiduNetdiskDownload\wechat.apk",
      "appPackage":"com.jiaozidt.appc",
      "appActivity":"io.dcloud.PandoraEntryActivity",
      # 解决输入中文
      "unicodeKeyboard":True,
      "resetKeyboard":True

      }
    return caps


# if __name__=="__main__":
#     dr=init_driver()
#     driver = webdriver.Remote(
#         # appium 端口号
#         command_executor='http://127.0.0.1:4723/wd/hub',
#         desired_capabilities=dr
#     )
#
#
#     loc = (MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("分类")')
#     WebDriverWait(driver, 20).until(EC.visibility_of_element_located(loc))
#     driver.find_element(*loc).click()
#
#     sleep(2)
#     # loc = (MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("搜索商家或商品名称")')
#     # WebDriverWait(driver, 20).until(EC.visibility_of_element_located(loc))
#     phone=driver.find_element(MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("搜索商家或商品名称")')
#     phone.click()
#     sleep(2)
#     driver.press_keycode(45)
#     phone = driver.find_element(MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("搜索")')
#     phone.click()
#     # 获取所有上下文
#     cons = driver.contexts
#     print(cons)
#     sleep(3)
#     # driver.press_keycode(8)
#     # driver.find_element(MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("没有搜索结果")').text()
#     # print(aaa)
#     driver.switch_to.context('WEBVIEW_com.lemon.lemonban')
#     print(driver.context)
#     sleep(2)
#
#     driver.find_element(MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("没有搜索结果")').text()
#
#
#
#     sleep(10)
#     quit()




