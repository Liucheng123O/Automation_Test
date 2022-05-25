from appium.webdriver.common.mobileby import MobileBy


class MerchantDetailLocs:
    """ 首页-商户详情页面元素  """
    #商户详情
    merchant_title=(MobileBy.ANDROID_UIAUTOMATOR,'new UiSelector().text("商户详情")')
    #商户详情-商户名称
    merchant_name=(MobileBy.ANDROID_UIAUTOMATOR,'new UiSelector().text("（椰云）APP自动化测试商户勿动1111~~")')
    #商户详情-商户区域
    merchant_area=(MobileBy.ANDROID_UIAUTOMATOR,'new UiSelector().text("武侯区")')
    #商户详情-营业时间
    business_hours = (MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("营业时间 9-23")')
    #商户详情-商户地址导航
    merchant_navigation=(MobileBy.ANDROID_UIAUTOMATOR,'new UiSelector().text("中海国际D座1703")')
    #返回上一级
    return_button=(MobileBy.ANDROID_UIAUTOMATOR,'/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.LinearLayout/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View[1]/android.view.View/android.view.View[1]/android.view.View/android.view.View')

    #商户详情-通用饭票
    common_meal=(MobileBy.ANDROID_UIAUTOMATOR,'new UiSelector().text("通用饭票")')
    #商户详情-折扣标题
    discount_title=(MobileBy.ANDROID_UIAUTOMATOR,'UiSelector().text("全店8.8折优惠")')
    #商户详情-购买可退标题
    purchase_back_title=(MobileBy.ANDROID_UIAUTOMATOR,'UiSelector().text("无忧购买，随时可退~！")')
    #商户详情-去使用
    employ_button=(MobileBy.ANDROID_UIAUTOMATOR,'new UiSelector().text("去使用")')
    #商户详情-0-7折扣饭票
    discount_meal07=(MobileBy.ANDROID_UIAUTOMATOR,'new UiSelector().text("0-7折饭票")')
    #商户详情-商品名称
    commodity_name07=(MobileBy.ANDROID_UIAUTOMATOR,'new UiSelector().text("测试商品不要动***~~~~")')
    #商户详情-购买价
    purchase_price07=(MobileBy.ANDROID_UIAUTOMATOR,'new UiSelector().text("6.67")')
    #商户详情-门店价
    shop_price07=(MobileBy.ANDROID_UIAUTOMATOR,'new UiSelector().text("￥12.3")')
    #商户详情-省钱
    save_money07=(MobileBy.ANDROID_UIAUTOMATOR,'new UiSelector().text("共省5.63元")')
    #商户详情-去下单
    order_buytton07=(MobileBy.ANDROID_UIAUTOMATOR,'new UiSelector().text("去下单")')
    #7-8.5折扣饭票
    discount_meal785 = (MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("7-8.5折饭票")')
    # 商户详情-商品名称 7-8.5折
    commodity_name785 = (MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("jjjjk你就看见你姐姐jioj尽量加快了")')
    # 商户详情-购买价 7-8.5折
    purchase_price785 = (MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("10.97")')
    # 商户详情-门店价 7-8.5折
    shop_price785 = (MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("￥13.99")')
    # 商户详情-省钱 7-8.5折
    save_money785 = (MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("共省3.02元")')
    #通用饭票页面-提示
    meal_hint=(MobileBy.ANDROID_UIAUTOMATOR,'new UiSelector().text("出示二维码付款，享受合作商家全店折扣")')
    #套餐提示
    combo_hint=(MobileBy.ANDROID_UIAUTOMATOR,'new UiSelector().text("测试商品不要动***~~~~")')















