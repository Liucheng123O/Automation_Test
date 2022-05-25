from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from JiaoZiDT_AppClient_PO.Common.basepage import BasePage
from JiaoZiDT_AppClient_PO.PageLocators.my_locs.my_locs import MyLocs

class MyPage(BasePage):
    def personal_center(self):
        return self.get_element_text(MyLocs.personal_center,'我的页面-查看标题')

    def user_name(self):
        return self.get_element_text(MyLocs.user_name,'我的页面-获取名称')

    def user_code(self):
        return self.get_element_text(MyLocs.user_code,'我的页面-获取账号')

    def universal_meal_ticket(self):
        return self.get_element_text(MyLocs.universal_meal_ticket,'我的页面-获取通用饭票字段')

    def province(self):
        self.click_element(MyLocs.province,'我的页面-点击已省按钮')

    def province_detail(self):
        return self.get_element_text(MyLocs.province_detail,'我的-省钱页面 获取省钱明细字段')

    def buy_ticket(self):
        self.click_element(MyLocs.buy_ticket,'我的页面-点击购买按钮')

    def buy_ticket_title(self):
        return self.get_element_text(MyLocs.buy_ticket_title,'我的-购买饭票页面 获取标题')

    def meal_ticket_money(self):
        return self.get_element_text(MyLocs.meal_ticket_money,'我的-购买饭票页面 获取充值金额字段')

    def retrea_ticket(self):
        self.click_element(MyLocs.retrea_ticket,'我的页面  点击退票按钮')

    def meal_ticket_refund(self):
        return self.get_element_text(MyLocs.meal_ticket_refund,'我的-退款页面 获取标题')

    def refund_caus(self):
        self.click_element(MyLocs.refund_caus,'我的-退款页面 点击退款原因')

    def slide_the_screen_refund(self):
        self.slide_the_screen(MyLocs.refund,'我的-退款页面 滑屏操作')

    def refund(self):
        self.click_element(MyLocs.refund,'我的-退款页面 点击退款按钮')

    def usage_record(self):
        self.click_element(MyLocs.usage_record,'我的页面-点击使用记录')

    def transaction_record(self):
        return self.get_element_text(MyLocs.transaction_record,'我的-使用记录页面 获取交易记录字段')

    def curren_ticket(self):
       return self.get_element_text(MyLocs.curren_ticket,'我的-使用记录页面 获取当前余票字段')

    def red_packet(self):
        self.click_element(MyLocs.red_packet,'我的页面-点击红包按钮')

    def backlog(self):
        return self.get_element_text(MyLocs.backlog,'我的-红包页面 获取待使用字段')

    def red_packet_name(self):
        return self.get_element_text(MyLocs.red_packet_name,'我的-红包页面 获取红包名称字段')

    def period_of_validity(self):
        return self.get_element_text(MyLocs.period_of_validity,'我的-红包页面 获取有效期字段')

    def no_threshold(self):
        return self.get_element_text(MyLocs.no_threshold,'我的-红包页面 获取无门槛字段')

    def red_packet_money(self):
        return self.get_element_text(MyLocs.red_packet_money,'我的-红包页面 获取红包金额字段')

    def detailed_rules(self):
        self.click_element(MyLocs.detailed_rules,'我的-红包页面 获取详细规则字段')

    def detailed_rules_details(self):
        return self.get_element_text(MyLocs.detailed_rules_details,'我的-红包页面 获取详细规则详情字段')

    def to_use_the(self):
        self.click_element(MyLocs.to_use_the,'我的-红包页面 点击去使用按钮')

    def red_packet_employ(self):
        return self.get_element_text(MyLocs.red_packet_employ,'我的-红包页面 获取可用商品字段')

    def have_been_used(self):
        self.click_element(MyLocs.have_been_used,'我的-红包页面 点击已使用')

    def examine(self):
        self.click_element(MyLocs.examine,'我的-红包页面 点击查看按钮')

    def commercial_name(self):
        return self.get_element_text(MyLocs.commercial_name,'我的-红包页面 获取商户名称')

    def have_expired(self):
        return self.get_element_text(MyLocs.have_expired,'我的-红包页面 获取已过期字段')

    def my_favorite(self):
        self.click_element(MyLocs.my_favorite,'我的页面 点击收藏')

    def merchant_name(self):
        return self.get_element_text(MyLocs.merchant_name,'我的-收藏页面 获取商品名称')

    def money(self):
        return self.get_element_text(MyLocs.money,'我的-收藏页面 获取价格')

    def title(self):
        return self.get_element_text(MyLocs.title,'我的-收藏页面 获取收藏字段')

    def management(self):
        self.click_element(MyLocs.management,'我的-收藏页面 点击管理 按钮')

    def accomplish(self):
        return self.get_element_text(MyLocs.accomplish,'我的-收藏页面 获取完成')

    def delete(self):
        return self.get_element_text(MyLocs.delete,'我的-收藏页面  获取删除')

    def integral_button(self):
        self.click_element(MyLocs.integral,'我的页面 点击我的积分')

    def integral_balance(self):
        return self.get_element_text(MyLocs.integral_balance,'我的-交子积分页面 获取积分余额字段')

    def integral_text(self):
        return self.get_element_text(MyLocs.integral,'我的页面 获取标题')

    def collect_integral(self):
        self.click_element(MyLocs.collect_integral,'我的-交子积分页面 点击收积分')
    def collect_integral_code(self):
        return self.get_element_text(MyLocs.collect_integral_code,'我的-交子积分页面 获取页面标题')

    def collect_integral_qr_code(self):
        return self.get_element_text(MyLocs.collect_integral_qr_code,'我的-交子积分页面 获取收积分二维码字段')

    def participation(self):
        self.click_element(MyLocs.participation,'我的-交子积分页面 点击立即参与')

    def search(self):
        return self.get_element_text(MyLocs.search,'分类页面 获取搜索字段')

    def transaction_record_integral_button(self):
        self.click_element(MyLocs.transaction_record_integral,'我的-交子积分页面 点击交易记录')

    def transaction_record_integral_text(self):
        return self.get_element_text(MyLocs.transaction_record_integral,'我的-交子积分页面 获取交易记录标题')

    def current_integral(self):
        return self.get_element_text(MyLocs.current_integral,'我的-交子积分页面 获取当前积分字段')

    def integral_recharge(self):
        self.click_element(MyLocs.integral_recharge,'我的-交子积分页面 点击积分卡充值')

    def password_recharge(self):
        return self.get_element_text(MyLocs.password_recharge,'我的-交子积分页面 获取标题')

    def recharge(self):
        return self.get_element_text(MyLocs.recharge,'我的-交子积分页面 获取充值字段')

    def binding_phone(self):
        self.click_element(MyLocs.binding_phone,'我的页面 点击绑定手机')

    def binding_phone_mark(self):
        return self.get_element_text(MyLocs.binding_phone_mark,'我的-绑定手机号页面 获取标题')

    def binding(self):
        return self.get_element_text(MyLocs.binding,'我的-绑定手机号页面 获取绑定字段')

    def about_us(self):
        self.click_element(MyLocs.about_us,'我的页面 点击关于我们')

    def about_jiaozi(self):
        return self.get_element_text(MyLocs.about_jiaozi,'我的-关于我们页面 获取关于交子饭票')

    def service_agreement(self):
        return self.get_element_text(MyLocs.service_agreement,'我的-关于我们页面 获取服务协议字段')

    def privacy_policy(self):
        return self.get_element_text(MyLocs.privacy_policy,'我的-关于我们页面 获取隐私政策字段')










































