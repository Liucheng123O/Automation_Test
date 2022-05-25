from appium.webdriver.common.mobileby import MobileBy


class SetMealDetailLocs:
    """ 首页-套餐详情 页面元素"""
    #商品标题
    meal_title=(MobileBy.ANDROID_UIAUTOMATOR,'new UiSelector().text("测试商品不要动***~~~~")')
    #套餐详情-页面标题
    title=(MobileBy.ANDROID_UIAUTOMATOR,'new UiSelector().text("套餐详情")')
    #套餐详情-购买价
    purchase_price = (MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("6.67")')
    #套餐详情-门店价
    shop_price = (MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("￥12.3")')
    #套餐详情-省钱
    save_money=(MobileBy.ANDROID_UIAUTOMATOR,'new UiSelector().text("￥5.63") ')
    #套餐详情-平台价字段
    terrace_field=(MobileBy.ANDROID_UIAUTOMATOR,'new UiSelector().text("平台价")')
    #原价
    original_price_field=(MobileBy.ANDROID_UIAUTOMATOR,'new UiSelector().text("门店原价")')
    #省钱字段
    money_money=(MobileBy.ANDROID_UIAUTOMATOR,'new UiSelector().text("省钱")')
    #过期自动退款提示
    refund_hint=(MobileBy.ANDROID_UIAUTOMATOR,'new UiSelector().text("无忧下单 随时可退 · 过期自动退")')
    #退款标题
    refund_title=(MobileBy.ANDROID_UIAUTOMATOR,'new UiSelector().text("无忧下单")')
    #未使用提示
    unused_hint=(MobileBy.ANDROID_UIAUTOMATOR,'new UiSelector().text("1.未使用时随时退款(免手续费)")')
    #过期提示
    past_due_title=(MobileBy.ANDROID_UIAUTOMATOR,'new UiSelector().text("2.过期未使用自动退款(免手续费)")')
    #使用有效期
    use_validity=(MobileBy.ANDROID_UIAUTOMATOR,'new UiSelector().text("使用有效期：2022-04-01 至 2023-05-20")')
    #可用时间
    usable_time=(MobileBy.ANDROID_UIAUTOMATOR,'new UiSelector().text("00:00-23:59")')
    #使用规则
    usable_rule=(MobileBy.ANDROID_UIAUTOMATOR,'new UiSelector().text("使用规则：")')
    #规则详情
    rule_details=(MobileBy.ANDROID_UIAUTOMATOR,'new UiSelector().text("很反感发给怼###￥￥￥￥￥……&*！@#￥%……&*（）（*&……%￥#@#￥%……&*（）））））（（（（（*****&&&…………%￥#@！@#￥%……&*（#￥5312323151123")')
    #展开
    unfold=(MobileBy.ANDROID_UIAUTOMATOR,'new UiSelector().text("展开")')
    #可用门店
    use_explain=(MobileBy.ANDROID_UIAUTOMATOR,'new UiSelector().text("可用门店")')
    #一个门店可用
    use_1explain=(MobileBy.ANDROID_UIAUTOMATOR,'new UiSelector().text("1个门店可用")')
    #可用门店标题
    use_1explain_title=(MobileBy.ANDROID_UIAUTOMATOR,'UiSelector().text("可用门店")')
    #商户名称
    commercial_name=(MobileBy.ANDROID_UIAUTOMATOR,'new UiSelector().text("（椰云）APP自动化测试商户勿动1111~~")')
    #品类
    category=(MobileBy.ANDROID_UIAUTOMATOR,'new UiSelector().text("武侯区 | 奶茶小吃")')
    #进店
    shop_button=(MobileBy.XPATH,'/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[2]/android.widget.FrameLayout[2]/android.widget.LinearLayout/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View[4]/android.view.View/android.view.View[2]')
    #导航地址
    navigation_site=(MobileBy.ANDROID_UIAUTOMATOR,'new UiSelector().text("中海国际D座1703")')
    #导航按钮
    navigation_button=(MobileBy.ANDROID_UIAUTOMATOR,'new UiSelector().text("navigation")')
    #进店 按钮
    shop=(MobileBy.ANDROID_UIAUTOMATOR,'new UiSelector().text("进店")')
    #使用说明
    instructions=(MobileBy.ANDROID_UIAUTOMATOR,'new UiSelector().text("使用说明")')
    #现在购买
    now_purchase=(MobileBy.ANDROID_UIAUTOMATOR,'new UiSelector().text("现在购买")')
    #到线下门店
    offline_shop=(MobileBy.ANDROID_UIAUTOMATOR,'new UiSelector().text("到线下门店")')
    #出示券码再消费
    show_coupon_code=(MobileBy.ANDROID_UIAUTOMATOR,'new UiSelector().text("出示券码再消费")')
    #套餐明细
    meal_detail=(MobileBy.ANDROID_UIAUTOMATOR,'new UiSelector().text("套餐明细")')
    #立即下单
    immediately_order=(MobileBy.ANDROID_UIAUTOMATOR,'new UiSelector().text("立即下单")')
    #下单金额
    #收藏
    collect=(MobileBy.ANDROID_UIAUTOMATOR,'new UiSelector().text("收藏")')
    #分享
    share=(MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("分享")')
    #确认订单
    affirm_order_text=(MobileBy.ANDROID_UIAUTOMATOR,'new UiSelector().text("确认订单")')
    #商品名称
    #免预约
    subscribe_text=(MobileBy.ANDROID_UIAUTOMATOR,'new UiSelector().text("周一到周日 免预约")')
    #随时退
    casual_retreat_text=(MobileBy.ANDROID_UIAUTOMATOR,'new UiSelector().text("随时退")')
    #过期退
    past_due_retreat_text=(MobileBy.ANDROID_UIAUTOMATOR,'new UiSelector().text("过期退")')
    #数量文本
    quantity_text=(MobileBy.ANDROID_UIAUTOMATOR,'new UiSelector().text("数量")')
    #数量
    quantity_value=(MobileBy.ANDROID_UIAUTOMATOR,'new UiSelector().text("1")')
    #红包优惠
    red_packet_text=(MobileBy.ANDROID_UIAUTOMATOR,'new UiSelector().text("红包/优惠券")')
    #红包金额
    red_packet_money=(MobileBy.ANDROID_UIAUTOMATOR,'new UiSelector().text("-￥5.9")')
    #红包金额-合计
    red_packet_money_total=(MobileBy.ANDROID_UIAUTOMATOR,'new UiSelector().text("合计￥0.77")')
    # 可用红包
    usable_red_packet = (MobileBy.ANDROID_UIAUTOMATOR,'new UiSelector().text("1 个红包可用")')
    #取消红包合计
    cancel_red_packet_total=(MobileBy.ANDROID_UIAUTOMATOR,'new UiSelector().text("合计￥6.67")')
    #红包名称
    red_packet_name=(MobileBy.ANDROID_UIAUTOMATOR,'new UiSelector().text("APP自动化测试红包 不要动")')




    #积分抵扣
    integral_deduction_text=(MobileBy.ANDROID_UIAUTOMATOR,'new UiSelector().text("积分抵扣")')
    #余额
    balance_text=(MobileBy.ANDROID_UIAUTOMATOR,'new UiSelector().text("（余额：")')
    #余额值
    balance_value=(MobileBy.ANDROID_UIAUTOMATOR,'new UiSelector().text("1000")')
    #积分
    integral_text=(MobileBy.ANDROID_UIAUTOMATOR,'new UiSelector().text("积分）")')
    #可用
    usable=(MobileBy.ANDROID_UIAUTOMATOR,'new UiSelector().text("可用")')
    #使用
    use=(MobileBy.ANDROID_UIAUTOMATOR,'new UiSelector().text("使用")')
    #积分值
    integral_value=(MobileBy.ANDROID_UIAUTOMATOR,'new UiSelector().text("请输入积分")')
    #积分，抵扣
    integraldeduction_text=(MobileBy.ANDROID_UIAUTOMATOR,'new UiSelector().text("积分，抵扣")')
    #元
    element=(MobileBy.ANDROID_UIAUTOMATOR,'new UiSelector().text("元")')




















