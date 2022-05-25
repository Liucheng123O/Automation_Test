import pytest

from JiaoZiDT_Web_PO.PageObjects.city_dining_page.enterprise_management_page import EnterpriseManagementPage


@pytest.mark.userfixres("init_city_dining")
# @pytest.mark.EnterpriseManagement
class Test_Enterprise_Management:
    @pytest.mark.EnterpriseManagement
    def test_creat_enterprise_success(self,init_city_dining):
        """  新增企业成功 """
        #进入添加 创建企业
        EnterpriseManagementPage(init_city_dining).add_city("(测试)阿里baba","四川","小刘",'"D:\测试勿动.png"','"D:\测试勿动.png"','"D:\测试勿动.png"')
        #判断
        assert EnterpriseManagementPage(init_city_dining).add_judge() == "新增"

    def test_enterprise_name_search_success(self,init_city_dining):
        """  企业名称 查询成功 """
        #输入企业名称
        EnterpriseManagementPage(init_city_dining).enterprise_name("（测试）城市食堂交子专用企业2")
        #点击搜索
        EnterpriseManagementPage(init_city_dining).search()
        #判断
        assert EnterpriseManagementPage(init_city_dining).get_data() == "共 1 条"

    def test_recharge_amount_success(self,init_city_dining):
        """  充值成功 """
        # 输入企业名称
        EnterpriseManagementPage(init_city_dining).enterprise_name("（测试）城市食堂交子专用企业2")
        # 点击搜索
        EnterpriseManagementPage(init_city_dining).search()
        #充值
        assert EnterpriseManagementPage(init_city_dining).recharge_amount(10) == 10

    def test_freeze_amount_success(self,init_city_dining):
        """  冻结成功 """
        # 输入企业名称
        EnterpriseManagementPage(init_city_dining).enterprise_name("（测试）城市食堂交子专用企业2")
        # 点击搜索
        EnterpriseManagementPage(init_city_dining).search()
        # 判断
        assert EnterpriseManagementPage(init_city_dining).freeze_amount(10)  == 10

    def test_unfreeze_amount_sccess(self,init_city_dining):
        """  解冻成功  """
        # 输入企业名称
        EnterpriseManagementPage(init_city_dining).enterprise_name("（测试）城市食堂交子专用企业2")
        # 点击搜索
        EnterpriseManagementPage(init_city_dining).search()
        # 判断
        assert EnterpriseManagementPage(init_city_dining).unfreeze_amount(10) == 10




