from time import sleep

from JiaoZiDT_AppClient_PO.Common.basepage import BasePage
from JiaoZiDT_AppClient_PO.PageLocators.home_locs.set_meal_detail_locs.set_meal_detail_locs import SetMealDetailLocs


class SetMealDetailPage(BasePage):
    """首页-套餐详情 页面对象"""
    def meal_title(self):
        self.get_element_text(SetMealDetailLocs.meal_title,'首页- 商品标题')

    def title(self):
        return self.get_element_text(SetMealDetailLocs.title,'首页-套餐先详情页 获取套餐标题 ')

    def purchase_price(self):
        return self.get_element_text(SetMealDetailLocs.purchase_price,'首页-套餐详情页 获取购买价格')

    def shop_price(self):
        return self.get_element_text(SetMealDetailLocs.shop_price,'首页-套餐详情页 获取门店价格')

    def save_money(self):
        return self.get_element_text(SetMealDetailLocs.save_money,'首页-套餐详情页 获取省钱价')

    def terrace_field(self):
        return self.get_element_text(SetMealDetailLocs.terrace_field,'首页-套餐详情页 获取平台价字段')

    def original_price_field(self):
        return self.get_element_text(SetMealDetailLocs.original_price_field,'首页-套餐详情页 获取原价字段')

    def money_money(self):
        return self.get_element_text(SetMealDetailLocs.money_money,'首页-套餐详情页 获取省钱字段')

    def refund_hint(self):
        self.click_element(SetMealDetailLocs.refund_hint,'首页-套餐详情页 进入无忧下单页面')

    def refund_title(self):
        return self.get_element_text(SetMealDetailLocs.refund_title,'首页-套餐详情页-无忧下单 获取页面标题')

    def unused_hint(self):
        return self.get_element_text(SetMealDetailLocs.unused_hint,'首页-套餐详情页-无忧下单 获取未使用随时退款字段')

    def past_due_title(self):
        return self.get_element_text(SetMealDetailLocs.past_due_title,'首页-套餐详情页-无忧下单 获取过期未使用字段')

    def use_validity(self):
        return self.get_element_text(SetMealDetailLocs.use_validity,'首页-套餐详情页 获取使用有效期')

    def usable_time(self):
        return self.get_element_text(SetMealDetailLocs.usable_time,'首页-套餐详情页 获取可用时间')

    def usable_rule(self):
        return self.get_element_text(SetMealDetailLocs.usable_rule,'首页-套餐详情页 获取使用规则')

    def slide_screen_use_explain(self):
        self.slide_the_screen(SetMealDetailLocs.use_explain,'首页-套餐详情页 滑屏找到”展开“按钮')

    def unfold(self):
        self.click_element(SetMealDetailLocs.unfold,'首页-套餐详情页 点击展开按钮')

    def rule_details(self):
        return self.get_element_text(SetMealDetailLocs.rule_details,'首页-套餐详情页 获取使用规则详细')

    def use_1explain(self):
        self.click_element(SetMealDetailLocs.use_1explain,'首页-套餐详情页 点击可用门店')

    def commercial_name(self):
        return self.get_element_text(SetMealDetailLocs.commercial_name,'首页-套餐详情-可用门店页 获取商户名称')

    def category(self):
        return self.get_element_text(SetMealDetailLocs.category,'首页-套餐详情-可用门店页 获取区域类别')

    def use_1explain_title(self):
        return self.get_element_text(SetMealDetailLocs.use_1explain_title,'首页-套餐详情-可用门店页 获取页面标题')

    def shop_button(self):
        self.click_element(SetMealDetailLocs.shop_button,'首页-套餐详情-可用门店页 点击进店按钮')

    def shop(self):
        self.click_element(SetMealDetailLocs.shop,'首页-套餐详情页 点击进店按钮')

    def navigation_site(self):
        return self.get_element_text(SetMealDetailLocs.navigation_site,'首页-套餐详情-可用门店页 获取导按地址')

    def navigation_button(self):
        self.click_element(SetMealDetailLocs.navigation_button,'首页-套餐详情 点击导航按钮')

    def slide_the_screen_instructions(self):
        self.slide_the_screen(SetMealDetailLocs.instructions,'首页-套餐详情 滑屏找到使用说明字段')

    def now_purchase(self):
        return self.get_element_text(SetMealDetailLocs.now_purchase,'首页-套餐详情 获取现在购买字段')

    def offline_shop(self):
        return self.get_element_text(SetMealDetailLocs.offline_shop,'首页-套餐详情 获取到线下门店字段')

    def show_coupon_code(self):
        return self.get_element_text(SetMealDetailLocs.show_coupon_code,'首页-套餐详情 获取出示券码再消费字段')

    def meal_detail(self):
        return self.get_element_text(SetMealDetailLocs.meal_detail,'首页-套餐详情 获取套餐明细字段')

    def immediately_order(self):
        return self.get_element_text(SetMealDetailLocs.immediately_order,'首页-套餐详情 获取立即下单字段')

    def collect(self):
        return self.get_element_text(SetMealDetailLocs.collect,'首页-套餐详情 获取收藏字段')

    def share(self):
        return self.get_element_text(SetMealDetailLocs.share,'首页-套餐详情 获取分享字段')

    def immediately_order_button(self):
        self.click_element(SetMealDetailLocs.immediately_order,'首页-套餐详情 点击立即下单按钮')

    def affirm_order_text(self):
        return self.get_element_text(SetMealDetailLocs.affirm_order_text,'首页-套餐详情 获取确认订单字段')

    def subscribe_text(self):
        return self.get_element_text(SetMealDetailLocs.subscribe_text,'首页-套餐详情 获取免预约字段')

    def casual_retreat_text(self):
        return self.get_element_text(SetMealDetailLocs.casual_retreat_text,'首页-套餐详情 获取随时退字段')

    def past_due_retreat_text(self):
        return self.get_element_text(SetMealDetailLocs.past_due_retreat_text,'首页-套餐详情 获取过期退字段')

    def quantity_text(self):
        return self.get_element_text(SetMealDetailLocs.quantity_text,'首页-套餐详情-确认订单页 获取数量字段')

    def quantity_walue(self):
        return self.get_element_text(SetMealDetailLocs.quantity_value,'首页-套餐详情-确认订单页 获取数量值')

    def red_packet_text(self):
        return self.get_element_text(SetMealDetailLocs.red_packet_text,'首页-套餐详情-确认订单页 获取红包/优惠券字段')

    def red_packet_money(self):
        return self.get_element_text(SetMealDetailLocs.red_packet_money,'首页-套餐详情-确认订单页 获取红包金额')

    def red_packet_money_total(self):
        return self.get_element_text(SetMealDetailLocs.red_packet_money_total,'首页-套餐详情-确认订单页 获取合计')

    def click_red_packet_money(self):
        self.click_element(SetMealDetailLocs.red_packet_money,'首页-套餐详情-确认订单页 点击红包金额')

    def red_packet_name(self):
        self.click_element(SetMealDetailLocs.red_packet_name,'首页-套餐详情-确认订单页 点击红包名称')

    # def cancel_red_packet_total(self):
    #     return self.get_element_text(SetMealDetailLocs.cancel_red_packet_total,'首页-套餐详情-确认订单页 获取合计金额')

    def usable_red_packet(self):
        return self.get_element_text(SetMealDetailLocs.usable_red_packet,'首页-套餐详情-确认订单页 获取是否有可用红包')




