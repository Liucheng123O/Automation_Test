# from datetime import time
# from selenium import webdriver
# screenshot_path="D:\pycharm\webauto_PO\Outputs\screensshots"
#
# def get_screenshot(self,name):
#     """截图"""
#     driver = webdriver.Chrome()
#     driver.maximize_window()
#     driver.implicitly_wait(6)
#     driver.get("https://www.baidu.com")
#     screenshot_time = time.strftime("%Y-%m-%d%H:%M")
#     return self.driver.get_screenshot_as_file(
#         screenshot_path +name  +screenshot_time+".png"
#     )
#
# import time
# from selenium import webdriver
#
# # def get_screenshot(self,screenshot_name):
# driver = webdriver.Chrome()
# driver.maximize_window()
# driver.implicitly_wait(6)
# driver.get("https://www.baidu.com")
# time.sleep(1)
# screenshot_time = time.strftime("%Y-%m-%d-%H_%M_%S")
# driver.get_screenshot_as_file("D:\pycharm\webauto_PO\Outputs\screensshots"+screenshot_time+".png")
# driver.quit()
import os

base_dir=os.path.split(os.path.split(os.path.abspath(__file__))[0])[0]

testdatas_dir=os.path.join(base_dir,"TestDatas")

testcases_dir=os.path.join(base_dir,"TestCases")


htmlreport_dir=os.path.join(base_dir,"Outputs/reports")
logs_dir=os.path.join(base_dir,"Outputs/logs")
# print(logs_dir)

screenshot_dir=os.path.join(base_dir,"Outputs/screenshots")
# print(screenshot_dir)



# base_dir=os.path.split(os.path.split(os.path.abspath(__file__))[0])[0]
#
# testdatas_dir = os.path.join(base_dir, "TestDatas")
# testcases_dir=os.path. join(base_dir, "TestCases")
#
# htmlreport_dir=os.path.join(base_dir, "Outputs/reports")
# logs_dir = os.path.join(base_dir, "Outputs/logs")
#
# # config dir = os.path. join(base dir, "Config")
# screenshot_dir = os.path. join(base_dir, "Outputs/screensshots")
# print(screenshot_dir)


