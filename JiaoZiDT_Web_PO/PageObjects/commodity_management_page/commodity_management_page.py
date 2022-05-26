from time import sleep

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

from JiaoZiDT_Web_PO.Common.basepage import BasePage
from JiaoZiDT_Web_PO.PageLocators.commodity_management_locs.commodity_management_locs import CommodityManagementLocs
from pywinauto import Desktop

class CommodityManagementPage(BasePage):
    def add_Commodity(self):
        self.click_element(CommodityManagementLocs.commoditymanagement1,'此首页页面-点击 商品管理2')
        self.click_element(CommodityManagementLocs.add_management,'商品新增页面--点击 新增')
        self.input_text(CommodityManagementLocs.affiliated_merchants, '(测试)鱼摆摆', '商品新增--输入名称', timeout=10)
        self.click_element(CommodityManagementLocs.click_commodity,"商品新增页面--点击 商户")
        self.input_text(CommodityManagementLocs.quantity_instock,'999',"商品新增页面--输入商品库存数量")
        self.input_text(CommodityManagementLocs.commodity_title,'（测试）测试商品勿动~~dukfhksdhf ffhasehfhfuifhaIWDHQWHDRUIHBGFHD ',"商品新增--商品标题")
        self.input_text(CommodityManagementLocs.set_name,'垃圾套餐','商品新增页面--输入 套餐名称')
        self.click_element(CommodityManagementLocs.uploading_picture, '商品新增页面--点击上传图片')

        app = Desktop()
        # 根据名字找到弹出窗口
        sleep(2)
        dialog = app["打开"]
        sleep(1)
        dialog["Edit"].type_keys("D:\测试勿动.png")
        sleep(1.5)
        dialog["Button"].click()
        self.input_text(CommodityManagementLocs.subheading, '勿动~~~', '商品新增页面--输入 商品套餐副标题')
        self.click_element(CommodityManagementLocs.classification1, '商品新增页面--点击 商品一级分类')
        self.click_element(CommodityManagementLocs.click_classification1, '商品新增页面--点击 美食')
        self.click_element(CommodityManagementLocs.classification2, '商品新增页面--点击 商品二级分类')
        self.click_element(CommodityManagementLocs.click_classification2, '商品新增页面--点击 快餐简餐',timeout=10)
        self.input_text(CommodityManagementLocs.include_solo,"没有", '商品新增页面--输入 包含单品')
        self.input_text(CommodityManagementLocs.solo_price,"6",'商品新增页面--输入 单品价格')
        self.input_text(CommodityManagementLocs.shop_price,"6", '商品新增页面--输入 门店价格')
        self.input_text(CommodityManagementLocs.help_price, "6", '商品新增页面--输入 帮抢价格')
        self.input_text(CommodityManagementLocs.price, "6", '商品新增页面--输入 单买价格')
        self.input_text(CommodityManagementLocs.service_regulations,"我是规则123456",'商品新增--输入规则')
        self.input_text(CommodityManagementLocs.floor_price, "5", '商品新增页面--输入 商家底价')
        self.click_element(CommodityManagementLocs.start_data_1, '商品新增页面--点击 使用有效期')
        self.click_element(CommodityManagementLocs.start_data, '商品新增页面--点击 开始日期')
        self.click_element(CommodityManagementLocs.date_closed, '商品新增页面--点击 结束日期')
        self.click_element(CommodityManagementLocs.start_time_1, '商品新增页面--点击 可用时间')
        # self.click_element(CommodityManagementLocs.start_time, '商品新增--输入 开始时间')
        # self.click_element(CommodityManagementLocs.time_closed, '商品新增--输入 结束时间')
        self.click_element(CommodityManagementLocs.confirm, '商品新增页面--点击 确定')
        self.click_element(CommodityManagementLocs.immediately_create, '商品新增页面--点击 立即创建')
    def create_successful_true(self):

        return self.get_element_text(CommodityManagementLocs.create_successful,"商品新增页面--创建成功",timeout=10)

    def select_commercial_name(self,neme):
        sleep(1)
        self.click_element(CommodityManagementLocs.commoditymanagement1, '此首页页面-点击 商品管理2')
        self.input_text(CommodityManagementLocs.commercial_name0,neme,"商品管理页面--输入商户名称",timeout=10)

    def commodity_quantity(self):
        sleep(1)
        self.click_element(CommodityManagementLocs.commoditymanagement1, '此首页页面-点击 商品管理2')
        return self.get_element_text(CommodityManagementLocs.commodity_quantity,'商品管理页面--查看商品数量条数')

    def no_data(self):
        return self.get_element_text(CommodityManagementLocs.no_data, '商品管理页面--查看商品数量条数(暂无数据)')

    def sort(self,sort1,sort2):
        sleep(1)
        self.click_element(CommodityManagementLocs.commoditymanagement1, '此首页页面-点击 商品管理2')
        self.input_text(CommodityManagementLocs.sort1,sort1,"商品管理页面--输入排序数字1")
        self.input_text(CommodityManagementLocs.sort2,sort2,"商品管理页面--输入排序数字2")

    def editor_sava(self):
        self.click_element(CommodityManagementLocs.editor,'商品管理页面--点击编辑按钮')
        self.click_element(CommodityManagementLocs.commodity_sava,"商品管理页面--点击保存按钮")

    def get_editor_sava_hint(self):
        return self.get_element_text(CommodityManagementLocs.sava_hint,'商品管理页面--正在获取 保存成功提示语')

    def commodity_type(self):
        sleep(1)
        self.click_element(CommodityManagementLocs.commoditymanagement1, '此首页页面-点击 商品管理2')
        self.click_element(CommodityManagementLocs.click_commodity_type,"商品管理页面--点击商品类型1")
        #下拉框
        sleep(2)
        ele=self.driver.find_element(By.XPATH, "//span[text()='汽车服务']")
        ActionChains(self.driver).move_to_element(ele).perform()
        self.click_element(CommodityManagementLocs.click_server0,'商品管理页面--点击汽车服务')

        # 鼠标悬浮，点击操作
        sleep(2)
        self.click_element(CommodityManagementLocs.click_commodity_type1,'商品管理页面--点击商品类型2')
        self.click_element(CommodityManagementLocs.click_commodity_type1, '商品管理页面--点击商品类型.1')
        self.click_element(CommodityManagementLocs.click_commodity_type1, '商品管理页面--点击商品类型2.2')
        ele2 = self.driver.find_element(By.XPATH, "//span[text()='其他']")
        ActionChains(self.driver).move_to_element(ele2).perform()
        self.click_element(CommodityManagementLocs.click_server1,'商品管理页面-- 选择其他')


    def search_button(self):
        self.click_element(CommodityManagementLocs.search, '商品管理页面--点击搜索')
        sleep(1)

    def commodity_close(self):
        self.click_element(CommodityManagementLocs.commodity_close,'商品管理页面--关闭商品')
        sleep(1)

    def commodity_open(self):
        self.click_element(CommodityManagementLocs.commodity_open,'商品管理页面--打开商品')

    def commodity_open_close_hint(self):
        return self.get_element_text(CommodityManagementLocs.close_open_hint,'商品管理页面--获取打开关闭商品提示语')























