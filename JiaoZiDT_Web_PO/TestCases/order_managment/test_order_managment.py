
""" 测试 订单管理页面 相关功能  """
from time import sleep

import pytest

from JiaoZiDT_Web_PO.PageObjects.order_managment_page.order_mangment_page import OrderManagementPage


@pytest.mark.usefixtures("init_order_management")
@pytest.mark.order
class Test_Order_Management:

    def test_useraccount_search_success(self,init_order_management):
        """ 使用 用户账号搜索成功 """
        #输入搜索 用户账号
        OrderManagementPage(init_order_management).user_account("17608001573555")
        #点击搜索
        OrderManagementPage(init_order_management).search_button()
        #判断 数据是否正确
        assert OrderManagementPage(init_order_management).user_data() == "共 9 条"

    def test_order_search_success(self,init_order_management):
        """ 通过订单号 进行查询成功 """
        #输入订单号
        OrderManagementPage(init_order_management).order("P1502114117035491328125")
        #点击搜索
        OrderManagementPage(init_order_management).search_button()
        #判断搜索条数
        assert OrderManagementPage(init_order_management).user_data() == "共 1 条"

    def test_merchant_search_success(self,init_order_management):
        """ 输入 商户名称 成功查询 """
        #输入商户名称
        OrderManagementPage(init_order_management).merchant_name("(测试)鱼摆摆")
        #点击搜索
        OrderManagementPage(init_order_management).search_button()
        #判断商户数据
        assert OrderManagementPage(init_order_management).user_data() == "共 2 条"

    def test_commodityname_search_success(self,init_order_management):
        """ 输入 商品名称 成功查询 """
        #输入商品名称
        OrderManagementPage(init_order_management).commodity_name("豆腐")
        #点击搜索
        OrderManagementPage(init_order_management).search_button()
        #判断商品条数
        assert OrderManagementPage(init_order_management).user_data() == "共 4 条"

    def test_payment_search_success(self,init_order_management):
        """ 查询 支付成功数据 """
        #点击 交易状态 -- 支付成功
        OrderManagementPage(init_order_management).deal_state()
        #点击搜索
        OrderManagementPage(init_order_management).search_button()
        #判断数据
        assert OrderManagementPage(init_order_management).user_data() != None

    def test_order_create_time_success(self,init_order_management):
        """ 选择 订单创建时间 查询成功 """
        #选择订单创建时间
        OrderManagementPage(init_order_management).order_create_time("2022-03-08","2022-03-10")
        #点击搜索
        OrderManagementPage(init_order_management).search_button()
        #判断数据条数
        assert OrderManagementPage(init_order_management).user_data() != None

    def test_mixture_select_success(self,init_order_management):
        """ 混合查询 用户账号、订单号、商户名称、商品名称 """
        # 输入搜索 用户账号
        OrderManagementPage(init_order_management).user_account("17608001573555")
        # 输入订单号
        OrderManagementPage(init_order_management).order("P1501863557690556416125")
        # 输入商户名称
        OrderManagementPage(init_order_management).merchant_name("（测试）快乐奶茶")
        # 输入商品名称
        OrderManagementPage(init_order_management).commodity_name("（测试）奶茶奶茶")
        #点击搜索
        OrderManagementPage(init_order_management).search_button()
        #判断数据条数
        assert OrderManagementPage(init_order_management).user_data() == "共 1 条"

    def test_mixture_select_fail(self,init_order_management):
        """  输入错误查询条件 输入失败 """
        # 输入搜索 用户账号
        OrderManagementPage(init_order_management).user_account("19138974297")
        # 输入订单号
        OrderManagementPage(init_order_management).order("P14878255519461539840")
        # 输入商户名称
        OrderManagementPage(init_order_management).merchant_name("椰云网络")
        # 输入商品名称
        OrderManagementPage(init_order_management).commodity_name("开发计划")
        # 点击搜索
        OrderManagementPage(init_order_management).search_button()
        # 判断数据条数
        assert OrderManagementPage(init_order_management).not_data() == "暂无数据"

    def test_open_detail_message_success(self,init_order_management):
        """  可成功进入 订单详情  """
        # 输入订单号
        OrderManagementPage(init_order_management).order("P1502114101231353856125")
        # 点击搜索
        OrderManagementPage(init_order_management).search_button()
        #点击详细按钮
        OrderManagementPage(init_order_management).detail_button()
        #判断是否进入详细页面
        assert OrderManagementPage(init_order_management).detail_message() == "订单详情"

    def test_default_show_data_success(self,init_order_management):
        #查询是否默认展示数据
        assert OrderManagementPage(init_order_management).user_data() != None
    # @pytest.mark.order
    # def test_select_page_success(self,init_order_management):
    #     """  通过翻页查找订单   """
    #     #点击页面
    #     OrderManagementPage(init_order_management).page_right_key()
    #     #判断是否跳转
    #     assert OrderManagementPage(init_order_management).get_order() == "P1501860817337843712124"

    # @pytest.mark.debug
    # def test_input_page_success(self,init_order_management):
    #     #输入页面
    #     OrderManagementPage(init_order_management).input_page(6)
    #     #点击搜索
    #     OrderManagementPage(init_order_management).search_button()
    #     #判断是否跳转
    #     assert OrderManagementPage(init_order_management).get_order() == "P1468508359635238912"








