import pytest
from JiaoZiDT_Web_PO.PageObjects.commodity_management_page.commodity_management_page import CommodityManagementPage
from JiaoZiDT_Web_PO.PageObjects.home_page import HomePage
"""  商品管理相关测试用例 """

@pytest.mark.usefixtures("init_commodity_management")
# @pytest.mark.CommodityManagement
class Test_Commodity_Management:
    @pytest.mark.CommodityManagement
    def test_add_ssuccess(self,init_commodity_management):
        """ 成功创建商品 """
        # 进入 商品管理
        # HomePage(init_commodity_management).management_home()
        #进入 商品新增页面
        CommodityManagementPage(init_commodity_management).add_Commodity()
        #判断是否创建成功
        assert CommodityManagementPage(init_commodity_management).create_successful_true() == "创建成功"

    def test_select_commercialname_success(self,init_commodity_management):
        """  商户名称 搜索成功 """
        # 进入 商品管理
        # HomePage(init_commodity_management).management_home()
        #商户名称  搜索
        CommodityManagementPage(init_commodity_management).select_commercial_name("（测试）快乐奶茶")
        CommodityManagementPage(init_commodity_management).search_button()
        #判断是否为3条数据
        assert CommodityManagementPage(init_commodity_management).commodity_quantity() == "共 2 条"

    def test_select_commercial_name_fail(self,init_commodity_management):
        """  查询商品名称条件为空 """
        # 进入 商品管理
        # HomePage(init_commodity_management).management_home()
        # 商户名称  搜索
        CommodityManagementPage(init_commodity_management).select_commercial_name("测试100")
        CommodityManagementPage(init_commodity_management).search_button()
        # 判断是否为3条数据
        assert CommodityManagementPage(init_commodity_management).no_data() == "暂无数据"

    def test_select_sort_success(self,init_commodity_management):
        """ 查询输入排序条件 搜索成功   """
        # 进入 商品管理
        # HomePage(init_commodity_management).management_home()
        #输入排序 数值
        CommodityManagementPage(init_commodity_management).sort("6","9")
        CommodityManagementPage(init_commodity_management).search_button()
        #判断条件数
        assert CommodityManagementPage(init_commodity_management).commodity_quantity() == "共 1 条"

    def test_editor_sava_success(self,init_commodity_management):
        """  商品编辑保存成功  """
        # 进入 商品管理
        # HomePage(init_commodity_management).management_home()
        #商户名称  搜索
        CommodityManagementPage(init_commodity_management).sort("6","7")
        #进入编辑 - 保存
        CommodityManagementPage(init_commodity_management).editor_sava()
        CommodityManagementPage(init_commodity_management).search_button()
        #判断是否成功
        assert CommodityManagementPage(init_commodity_management).get_editor_sava_hint() == "保存成功"

    def test_commodity_type_search_success(self,init_commodity_management):
        """ 通过商品类型进行搜索成功 """
        # 进入 商品管理
        # HomePage(init_commodity_management).management_home()
        #商品类型搜索
        CommodityManagementPage(init_commodity_management).commodity_type()
        CommodityManagementPage(init_commodity_management).search_button()
        #判断
        assert CommodityManagementPage(init_commodity_management).commodity_quantity() == "共 1 条"

    def test_combination_search_success(self,init_commodity_management):
        """ 组合搜索成功  """
        # 进入 商品管理
        # HomePage(init_commodity_management).management_home()
        #输入商户名称
        CommodityManagementPage(init_commodity_management).select_commercial_name("钵钵鸡")
        # 输入排序 数值
        CommodityManagementPage(init_commodity_management).sort("6", "9")
        # 商品类型搜索
        CommodityManagementPage(init_commodity_management).commodity_type()
        #搜索
        CommodityManagementPage(init_commodity_management).search_button()
        # 判断
        assert CommodityManagementPage(init_commodity_management).commodity_quantity() == "共 1 条"

    def test_commodity_stateswitch_success(self,init_commodity_management):
        """  成功上下架商品  """
        # 进入 商品管理
        # HomePage(init_commodity_management).management_home()
        # 输入商户名称
        CommodityManagementPage(init_commodity_management).select_commercial_name("钵钵鸡")
        # 输入排序 数值
        CommodityManagementPage(init_commodity_management).sort("6", "9")
        # 商品类型搜索
        CommodityManagementPage(init_commodity_management).commodity_type()
        # 搜索
        CommodityManagementPage(init_commodity_management).search_button()
        #关闭状态
        CommodityManagementPage(init_commodity_management).commodity_open()
        #判断关闭获取提示语
        assert CommodityManagementPage(init_commodity_management).commodity_open_close_hint() == "修改成功"
        #刷新页面
        init_commodity_management.refresh()
        # 商品类型搜索
        CommodityManagementPage(init_commodity_management).commodity_type()
        #点击关闭
        CommodityManagementPage(init_commodity_management).commodity_open()
        #判断开启获取提示语
        assert CommodityManagementPage(init_commodity_management).commodity_open_close_hint() == "修改成功"
        # 点击开启
        CommodityManagementPage(init_commodity_management).commodity_close()

    def test_default_show_data(self,init_commodity_management):
        " 进入商品管理页面，默认展示数据 "
        # 进入 商品管理
        # HomePage(init_commodity_management).management_home()
        assert CommodityManagementPage(init_commodity_management).commodity_quantity() != None

























