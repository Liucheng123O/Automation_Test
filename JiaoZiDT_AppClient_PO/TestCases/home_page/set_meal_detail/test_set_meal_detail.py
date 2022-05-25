import pytest

from JiaoZiDT_AppClient_PO.PageObjects.home_page.home_page import HomePage
from JiaoZiDT_AppClient_PO.PageObjects.home_page.merchant_detail_page.merchant_detail_page import MerchantDetailPage
from JiaoZiDT_AppClient_PO.PageObjects.home_page.set_meal_detail_page.set_meal_detail_page import SetMealDetailPage


@pytest.mark.usefixtures("init_set_meal_detail")
# @pytest.mark.setmealdetail
class TestSetMealDetail:
    """首页-套餐详情 页面相关用例"""
    def test_meal_price_success(self,init_set_meal_detail):
        """
        首页-套餐详情 正确显示套餐详情、门店价格、原价、购买价、平台价字段【011】
        [Tags]   S
        [Documentation]
        ...    前置条件：
        ...    操作步骤：
        ...    1.使用用户端登录成功
        ...    2.点击首页,进入套餐详情
        ...    3.查看 套餐详情、门店价格、原价、购买价、平台价字段 字段展示
        ...    预期结果：
        ...    3.套餐详情、门店价格、原价、购买价、平台价字段 字段展示成功且正确
        """
        #判断套餐标题
        assert SetMealDetailPage(init_set_meal_detail).title() == '套餐详情'
        #判断购买价格
        assert SetMealDetailPage(init_set_meal_detail).purchase_price() == '6.67'
        #门店价格
        assert SetMealDetailPage(init_set_meal_detail).shop_price() == '￥12.3'
        #省钱价格
        assert SetMealDetailPage(init_set_meal_detail).save_money() == '￥5.63'
        #平台价字段
        assert SetMealDetailPage(init_set_meal_detail).terrace_field() == '平台价'
        #原价字段
        assert SetMealDetailPage(init_set_meal_detail).original_price_field() == '门店原价'
        #省钱字段
        assert SetMealDetailPage(init_set_meal_detail).money_money() == '省钱'

    def test_refund_hint_success(self,init_set_meal_detail):
        """
        首页-套餐详情-无忧下单 正确显示无忧下单页面字段【012】
        [Tags]   S
        [Documentation]
        ...    前置条件：
        ...    操作步骤：
        ...    1.使用用户端登录成功
        ...    2.点击首页,进入套餐详情，再进入无忧下单
        ...    3.查看字段展示
        ...    预期结果：
        ...    3.成功跳转该页面且页面字段展示正确
        """
        #点击进入退款提示页面
        SetMealDetailPage(init_set_meal_detail).refund_hint()
        #判断页面标题
        assert SetMealDetailPage(init_set_meal_detail).refund_title() == '无忧下单'
        #判断未使用标题
        assert SetMealDetailPage(init_set_meal_detail).unused_hint() == '1.未使用时随时退款(免手续费)'
        #判断过期标题
        assert SetMealDetailPage(init_set_meal_detail).past_due_title() =='2.过期未使用自动退款(免手续费)'

    def test_meal_rule_success(self,init_set_meal_detail):
        """
        首页-套餐详情 正确显示使用有效期、可用时间、使用规则、展开按钮、规则详情【013】
        [Tags]   S
        [Documentation]
        ...    前置条件：
        ...    操作步骤：
        ...    1.使用用户端登录成功
        ...    2.点击首页,进入套餐详情
        ...    3.查看字段展示 使用有效期、可用时间、使用规则、展开按钮、规则详情
        ...    预期结果：
        ...    3.使用有效期、可用时间、使用规则、展开按钮、规则详情 正确展示
        """
        #判断使用有效期
        assert SetMealDetailPage(init_set_meal_detail).use_validity() == '使用有效期：2022-04-01 至 2023-05-20'
        #可用时间
        assert SetMealDetailPage(init_set_meal_detail).usable_time() == '00:00-23:59'
        #使用规则
        assert SetMealDetailPage(init_set_meal_detail).usable_rule() == '使用规则：'
        #滑屏操作
        SetMealDetailPage(init_set_meal_detail).slide_screen_use_explain()
        #展开按钮
        SetMealDetailPage(init_set_meal_detail).unfold()
        #规则详情
        assert SetMealDetailPage(init_set_meal_detail).rule_details() , '很反感发给怼###￥￥￥￥￥……&*！@#￥%……&*（）（*&……%￥#@#￥%……&*（）））））（（（（（*****&&&…………%￥#@！@#￥%……&*（#￥53123'

    def test_usable_shop_success(self,init_set_meal_detail):
        """
        首页-套餐详情 正确显示可用门店、标题、地址【014】
        [Tags]   S
        [Documentation]
        ...    前置条件：
        ...    操作步骤：
        ...    1.使用用户端登录成功
        ...    2.点击首页,进入套餐详情
        ...    3.查看字段展示 可用门店、标题、地址
        ...    预期结果：
        ...    3.可用门店、标题、地址 正确展示
        """
        #滑动屏幕
        SetMealDetailPage(init_set_meal_detail).slide_screen_use_explain()
        #点击可用门店
        SetMealDetailPage(init_set_meal_detail).use_1explain()
        #判断标题
        assert SetMealDetailPage(init_set_meal_detail).use_1explain_title() == '可用门店'
        #判断商户
        assert SetMealDetailPage(init_set_meal_detail).commercial_name() == '（椰云）APP自动化测试商户勿动1111~~'
        #判断地址
        assert SetMealDetailPage(init_set_meal_detail).navigation_site() , '中海国际D座'
        #点击进店
        SetMealDetailPage(init_set_meal_detail).shop_button()
        #判断商户
        assert MerchantDetailPage(init_set_meal_detail).merchant_area() == '武侯区'

    def test_shop_message_success(self,init_set_meal_detail):
        """
        首页-套餐详情 正确显示商户名称、区域类别、跳转到可用门店【015】
        [Tags]   S
        [Documentation]
        ...    前置条件：
        ...    操作步骤：
        ...    1.使用用户端登录成功
        ...    2.点击首页,进入套餐详情
        ...    3.查看字段展示 商户名称、区域类别
        ...    4.点击门店跳转
        ...    预期结果：
        ...    3.商户名称、区域类别 正确展示
        ...    4.门店跳转成功
        """
        # 滑动屏幕
        SetMealDetailPage(init_set_meal_detail).slide_screen_use_explain()
        #商户名称
        assert SetMealDetailPage(init_set_meal_detail).commercial_name() == '（椰云）APP自动化测试商户勿动1111~~'
        #判断区域类别
        assert SetMealDetailPage(init_set_meal_detail).category() == '武侯区 | 奶茶小吃'
        #进店按钮
        SetMealDetailPage(init_set_meal_detail).shop()
        #判断是否跳转到可用门店
        assert MerchantDetailPage(init_set_meal_detail).merchant_area() == '武侯区'

    def test_navigation_button(self,init_set_meal_detail):
        """
        首页-套餐详情 可成功进入导航页面【015】
        [Tags]   S
        [Documentation]
        ...    前置条件：
        ...    操作步骤：
        ...    1.使用用户端登录成功
        ...    2.点击首页,进入套餐详情
        ...    3.点击导航按钮
        ...    预期结果：
        ...    3.成功跳转导航页面
        """
        #滑动屏幕
        SetMealDetailPage(init_set_meal_detail).slide_screen_use_explain()
        #导航地址
        SetMealDetailPage(init_set_meal_detail).navigation_button()
        #判断进入导航页面
        HomePage(init_set_meal_detail).click_navigation()
        # 获取取消按钮
        assert HomePage(init_set_meal_detail).cancel() == '取消'

    def test_instructions_success(self,init_set_meal_detail):
        """
        首页-套餐详情 套餐明细字段展示正确【016】
        [Tags]   S
        [Documentation]
        ...    前置条件：
        ...    操作步骤：
        ...    1.使用用户端登录成功
        ...    2.点击首页,进入套餐详情
        ...    3.查看套餐明细字段，现在购买、线下门店、出示券码再消费、套餐明细
        ...    预期结果：
        ...    3.成功正确展示现在购买、线下门店、出示券码再消费、套餐明细字段
        """
        #滑动屏幕
        SetMealDetailPage(init_set_meal_detail).slide_the_screen_instructions()
        #判断现在购买
        assert SetMealDetailPage(init_set_meal_detail).now_purchase() == '现在购买'
        #到线下门店
        assert SetMealDetailPage(init_set_meal_detail).offline_shop() == '到线下门店'
        #出示券码再消费
        assert SetMealDetailPage(init_set_meal_detail).show_coupon_code() == '出示券码再消费'
        #判断套餐明细
        assert SetMealDetailPage(init_set_meal_detail).meal_detail() == '套餐明细'

    def test_immediately_order_success(self,init_set_meal_detail):
        """
        首页-套餐详情 立即下单、收藏、分享、价格字段展示正确【017】
        [Tags]   S
        [Documentation]
        ...    前置条件：
        ...    操作步骤：
        ...    1.使用用户端登录成功
        ...    2.点击首页,进入套餐详情
        ...    3.查看套餐明细字段，立即下单、收藏、分享、价格
        ...    预期结果：
        ...    3.成功正确展示 立即下单、收藏、分享、价格
        """
        #判断立即下单
        assert SetMealDetailPage(init_set_meal_detail).immediately_order() == '立即下单'
        #判断收藏
        assert SetMealDetailPage(init_set_meal_detail).collect() == '收藏'
        #判断分享
        assert SetMealDetailPage(init_set_meal_detail).share() == '分享'
        #判断价格
        assert SetMealDetailPage(init_set_meal_detail).purchase_price() == '6.67'

    def test_affirm_order_info_success(self,init_set_meal_detail):
        """
        首页-套餐详情-确认订单 确认订单、预约、随时退、购买价格字段展示正确【018】
        [Tags]   S
        [Documentation]
        ...    前置条件：
        ...    操作步骤：
        ...    1.使用用户端登录成功
        ...    2.点击首页,进入套餐详情再进入确认订单页
        ...    3.查看确认订单字段，确认订单、预约、随时退、购买价格字段展示
        ...    预期结果：
        ...    3.成功正确展示 确认订单、预约、随时退、购买价格字段展示字段
        """
        #进入确认订单页面
        SetMealDetailPage(init_set_meal_detail).immediately_order_button()
        #判断确认订单
        assert SetMealDetailPage(init_set_meal_detail).affirm_order_text() == '确认订单'
        #判断预约
        assert SetMealDetailPage(init_set_meal_detail).subscribe_text() == '周一到周日 免预约'
        #判断随时退
        assert SetMealDetailPage(init_set_meal_detail).casual_retreat_text() == '随时退'
        #判断过期退
        assert SetMealDetailPage(init_set_meal_detail).past_due_retreat_text() == '过期退'
        #判断购买价格
        assert SetMealDetailPage(init_set_meal_detail).purchase_price() == '6.67'

    def test_defaul_use_red_packet_success(self,init_set_meal_detail):
        """
        首页-套餐详情-确认订单 数量、数量值、红包/优惠券、红包使用金额、合计金额字段展示正确【019】
        [Tags]   S
        [Documentation]
        ...    前置条件：
        ...    操作步骤：
        ...    1.使用用户端登录成功
        ...    2.点击首页,进入套餐详情再进入确认订单页
        ...    3.查看确认订单字段，数量、数量值、红包/优惠券、红包使用金额、合计金额字段展示
        ...    预期结果：
        ...    3.成功正确展示 数量、数量值、红包/优惠券、红包使用金额、合计金额展示字段
        """
        # 进入确认订单页面
        SetMealDetailPage(init_set_meal_detail).immediately_order_button()
        #判断数量文本
        assert SetMealDetailPage(init_set_meal_detail).quantity_text() == '数量'
        #判断数量值
        assert SetMealDetailPage(init_set_meal_detail).quantity_walue() == '1'
        #判断红包/优惠券文本
        assert SetMealDetailPage(init_set_meal_detail).red_packet_text() == '红包/优惠券'
        #判断红包使用金额
        assert SetMealDetailPage(init_set_meal_detail).red_packet_money() == '-￥5.9'
        #判断合计金额
        assert SetMealDetailPage(init_set_meal_detail).red_packet_money_total() == '合计￥0.77'

    @pytest.mark.setmealdetail
    def test_cancel_red_packet_success(self,init_set_meal_detail):
        """
        首页-套餐详情-确认订单 红包金额、红包名称、合计金额、红包使用金额、可用红包字段展示正确【019】
        [Tags]   S
        [Documentation]
        ...    前置条件：
        ...    操作步骤：
        ...    1.使用用户端登录成功
        ...    2.点击首页,进入套餐详情再进入确认订单页
        ...    3.查看确认订单字段，红包金额、红包名称、合计金额、红包使用金额、可用红包字段展示
        ...    预期结果：
        ...    3.成功正确展示 红包金额、红包名称、合计金额、红包使用金额、可用红包
        """
        # 进入确认订单页面
        SetMealDetailPage(init_set_meal_detail).immediately_order_button()
        #点击红包金额
        SetMealDetailPage(init_set_meal_detail).click_red_packet_money()
        #点击红包名称
        SetMealDetailPage(init_set_meal_detail).red_packet_name()
        #判断合计金额
        # assert SetMealDetailPage(init_set_meal_detail).cancel_red_packet_total() == '合计￥6.67'
        #判断可用红包
        assert SetMealDetailPage(init_set_meal_detail).usable_red_packet() == '1 个红包可用'














