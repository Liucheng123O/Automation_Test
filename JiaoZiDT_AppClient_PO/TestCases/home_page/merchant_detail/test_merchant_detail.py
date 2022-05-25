import pytest

from JiaoZiDT_AppClient_PO.PageObjects.home_page.home_page import HomePage
from JiaoZiDT_AppClient_PO.PageObjects.home_page.merchant_detail_page.merchant_detail_page import MerchantDetailPage


@pytest.mark.usefixtures("init_merchant_detail")
# @pytest.mark.merchantdetail
class TestMerchantDetail:
    """ 商户详情页面相关用例"""
    def test_merchant_message_success(self,init_merchant_detail):
        """
        首页-商户详情 正确显示商户标题、商户名称、营业时间、蓝票标题【07】
        [Tags]   S
        [Documentation]
        ...    前置条件：
        ...    操作步骤：
        ...    1.使用用户端登录成功
        ...    2.点击首页进入商户详情
        ...    3.查看 商户标题、商户名称、营业时间、蓝票标题
        ...    预期结果：
        ...    3.商户标题、商户名称、营业时间、蓝票标题 显示正确
        """
        #判断商户标题
        assert MerchantDetailPage(init_merchant_detail).merchant_title() == '商户详情'
        #判断商户名称
        assert MerchantDetailPage(init_merchant_detail).merchant_name() == '（椰云）APP自动化测试商户勿动1111~~'
        #判断区域
        assert MerchantDetailPage(init_merchant_detail).merchant_area() == '武侯区'
        #判断营业时间
        assert MerchantDetailPage(init_merchant_detail).business_hours() == '营业时间 9-23'
        #判断通用饭票蓝票标题
        assert MerchantDetailPage(init_merchant_detail).common_meal() == '通用饭票'

    def test_discount_details07_success(self,init_merchant_detail):
        """
        首页-商户详情 正确显示折扣优惠、0-7折扣饭票、门店价格、购买价格【08】
        [Tags]   S
        [Documentation]
        ...    前置条件：
        ...    操作步骤：
        ...    1.使用用户端登录成功
        ...    2.点击首页进入商户详情
        ...    3.查看 折扣优惠、0-7折扣饭票、门店价格、购买价格
        ...    预期结果：
        ...    3.折扣优惠、0-7折扣饭票、门店价格、购买价格 显示正确
        """
        #滑动屏幕
        MerchantDetailPage(init_merchant_detail).swipe_screen()
        #获取折扣优惠8.8折
        assert MerchantDetailPage(init_merchant_detail).discount_title() == '全店8.8折优惠'
        #获取无忧购买
        assert MerchantDetailPage(init_merchant_detail).purchase_back_title() == '无忧购买，随时可退~！'
        #判断0-7折扣饭票
        assert MerchantDetailPage(init_merchant_detail).discount_meal07() == '0-7折饭票'
        #判断商品名称
        assert MerchantDetailPage(init_merchant_detail).commodity_name07() == '测试商品不要动***~~~~'
        #判断购买价格
        assert MerchantDetailPage(init_merchant_detail).purchase_price07() == '6.67'
        #判断门店价格
        assert MerchantDetailPage(init_merchant_detail).shop_price07() == '￥12.3'
        #判断共省钱
        assert MerchantDetailPage(init_merchant_detail).save_money07() == '共省5.63元'

    def test_discount_details785_success(self, init_merchant_detail):
        """
        首页-商户详情 正确显示7-8.5折扣饭票、商户名称、购买价格、门店价格、共省钱【09】
        [Tags]   S
        [Documentation]
        ...    前置条件：
        ...    操作步骤：
        ...    1.使用用户端登录成功
        ...    2.点击首页进入商户详情
        ...    3.查看 7-8.5折扣饭票、商户名称、购买价格、门店价格、共省钱
        ...    预期结果：
        ...    3.7-8.5折扣饭票、商户名称、购买价格、门店价格、共省钱 显示正确
        """
        #滑动屏幕
        MerchantDetailPage(init_merchant_detail).swipe_screen()
        #判断7-8.5折扣饭票
        assert MerchantDetailPage(init_merchant_detail).discount_meal785() == '7-8.5折饭票'
        #判断商品名称
        assert MerchantDetailPage(init_merchant_detail).commodity_name785() == 'jjjjk你就看见你姐姐jioj尽量加快了'
        #判断购买价格
        assert MerchantDetailPage(init_merchant_detail).purchase_price785() == '10.97'
        #判断门店价格
        assert MerchantDetailPage(init_merchant_detail).shop_price785() == '￥13.99'
        #判断共省钱
        assert MerchantDetailPage(init_merchant_detail).save_money785() == '共省3.02元'

    def test_merchant_jump_meal(self,init_merchant_detail):
        """
        首页-商户详情 点击去使用 可以跳转到蓝票页面【10】
        [Tags]   S
        [Documentation]
        ...    前置条件：
        ...    操作步骤：
        ...    1.使用用户端登录成功
        ...    2.点击首页进入商户详情再点击去使用
        ...    预期结果：
        ...    2.成功跳转到蓝票页面
        """
        #点击去使用按钮
        MerchantDetailPage(init_merchant_detail).employ_button()
        #获取饭票页面提示
        assert MerchantDetailPage(init_merchant_detail).meal_hint() == '出示二维码付款，享受合作商家全店折扣'

    def test_merchant_jump_combo(self,init_merchant_detail):
        """
        首页-商户详情 点击去下单 可以跳转到套餐详情【11】
        [Tags]   S
        [Documentation]
        ...    前置条件：
        ...    操作步骤：
        ...    1.使用用户端登录成功
        ...    2.点击首页进入商户详情再点击去下单
        ...    预期结果：
        ...    2.成功跳转到套餐详情页面
        """
        #滑屏操作
        MerchantDetailPage(init_merchant_detail).swipe_screen()
        #点击去下单按钮
        MerchantDetailPage(init_merchant_detail).order_button()
        #获取套餐提示
        assert MerchantDetailPage(init_merchant_detail).combo_hint() , '测试商品不要动'



