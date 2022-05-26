from time import sleep

from JiaoZiDT_Web_PO.Common.basepage import BasePage
from JiaoZiDT_Web_PO.PageLocators.city_dining_locs.enterprise_management_locs import EnterpriseManagementlocs


class EnterpriseManagementPage(BasePage):

    def add_city(self,enterprise_name,address,person_name,dir,id1,id2):
        self.click_element(EnterpriseManagementlocs.enterprise_management,'城市食堂-企业管理页面-- 进入企业管理')
        self.click_element(EnterpriseManagementlocs.add_city,'城市食堂-企业管理页面-- 点击添加企业')
        sleep(0.5)
        self.input_text(EnterpriseManagementlocs.add_enterprise_name,enterprise_name,"城市食堂-企业管理页面-- 输入企业名称")
        sleep(0.5)
        self.input_text(EnterpriseManagementlocs.add_enterprise_address,address,"城市食堂-企业管理页面-- 输入企业地址")
        sleep(1)
        self.input_text(EnterpriseManagementlocs.add_legal_person_name,person_name,'城市食堂-企业管理页面-- 输入法人姓名')
        sleep(1)
        self.upload_photo(EnterpriseManagementlocs.add_business_license,dir,"城市食堂-企业管理页面-- 上传营业执照")
        sleep(2)
        self.upload_photo(EnterpriseManagementlocs.add_id_number1,id1,'城市食堂-企业管理页面--上传身份证反面1')
        sleep(2)
        self.upload_photo(EnterpriseManagementlocs.add_id_number2, id2, '城市食堂-企业管理页面--上传身份证反面')
        sleep(2)
        self.input_text(EnterpriseManagementlocs.opening_bank,"成都很行",'城市食堂-企业管理页面-- 输入开户行')
        self.input_text(EnterpriseManagementlocs.bank_card,"6203156156987456",'城市食堂-企业管理页面-- 输入银行卡号')
        self.click_element(EnterpriseManagementlocs.add_creat,"城市食堂-企业管理页面-- 点击创建")

    def add_judge(self):
        return self.get_element_text(EnterpriseManagementlocs.add_city, '城市食堂-企业管理页面-- 点击添加企业')

    def enterprise_name(self,name):
        self.click_element(EnterpriseManagementlocs.enterprise_management, '城市食堂-企业管理页面-- 进入企业管理')
        self.input_text(EnterpriseManagementlocs.enterprise_name,name,"城市食堂-企业管理页面-- 输入企业名称")

    def search(self):
        self.click_element(EnterpriseManagementlocs.search,'城市食堂-企业管理页面-- 点击搜索按钮')

    def get_data(self):
        return self.get_element_text(EnterpriseManagementlocs.data,'城市食堂-企业管理页面-- 获取数据总数')

    def recharge_amount(self,amount):
        sleep(0.5)
        recharge_front=self.get_element_text(EnterpriseManagementlocs.get_amount,'城市食堂-企业管理页面--获取金额')
        # sleep(0.5)
        self.click_element(EnterpriseManagementlocs.recharge_button,'城市食堂-企业管理页面-- 点击充值按钮')
        self.input_text(EnterpriseManagementlocs.recharge_amount,amount,'城市食堂-企业管理页面--输入金额')
        self.click_element(EnterpriseManagementlocs.recharge_confirm,'城市食堂-企业管理页面--点击确定')
        sleep(0.5)
        recharge_queen=self.get_element_text(EnterpriseManagementlocs.get_amount, '城市食堂-企业管理页面--获取金额')
        return float(recharge_queen)-float(recharge_front)

    def freeze_amount(self,amount):
        sleep(0.5)
        recharge_front = self.get_element_text(EnterpriseManagementlocs.get_freeze_amount, '城市食堂-企业管理页面--获取冻结金额')
        # sleep(0.5)
        self.click_element(EnterpriseManagementlocs.freeze_button, '城市食堂-企业管理页面-- 点击冻结按钮')
        self.input_text(EnterpriseManagementlocs.recharge_amount,amount, '城市食堂-企业管理页面--输入冻结金额')
        self.click_element(EnterpriseManagementlocs.recharge_confirm, '城市食堂-企业管理页面--点击确定')
        sleep(0.5)
        recharge_queen = self.get_element_text(EnterpriseManagementlocs.get_freeze_amount, '城市食堂-企业管理页面--获取金额')
        return float(recharge_queen) - float(recharge_front)

    def unfreeze_amount(self,amount):
        sleep(0.5)
        recharge_front = self.get_element_text(EnterpriseManagementlocs.get_freeze_amount, '城市食堂-企业管理页面--获取冻结金额')
        # sleep(0.5)
        self.click_element(EnterpriseManagementlocs.unfreeze_button, '城市食堂-企业管理页面-- 点击解冻按钮')
        self.input_text(EnterpriseManagementlocs.recharge_amount, amount, '城市食堂-企业管理页面--输入解冻金额')
        self.click_element(EnterpriseManagementlocs.recharge_confirm, '城市食堂-企业管理页面--点击确定')
        sleep(0.5)
        recharge_queen = self.get_element_text(EnterpriseManagementlocs.get_freeze_amount, '城市食堂-企业管理页面--获取金额')
        return float(recharge_front) - float(recharge_queen)







