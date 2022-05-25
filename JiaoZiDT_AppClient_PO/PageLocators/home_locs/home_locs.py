from appium.webdriver.common.mobileby import MobileBy


class HomeLocs:
    # 商户名称
    merchants_name = (MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("（椰云）APP自动化测试商户勿动1111~~")')
    # 商户地址
    merchants_address = (MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("中海国际D座1703")')
    # 套餐名称
    setmeal_name = (MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("，测试套餐6666###%%%！！！")')
    # 通用饭票
    meal = (MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("，通用饭票")')
    # 爆品折扣
    explosive_discount = (MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("5.4折")')
    # 蓝票折扣
    Blue_discount = (MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("8.8折")')
    # 定位
    place = (MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("329 m")')
    # 商品副标题
    commodity_title = (MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("测试商品不要动***~~~~")')
    # 购买价
    purchase_price = (MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("6.67")')
    # 原价
    original_price = (MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("￥12.3")')
    # 热度
    heat = (MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("热度")')
    # 热度数
    heat_number = (MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("4.0")')

    #导航-商户名称
    commercial_name = (MobileBy.ACCESSIBILITY_ID, '（椰云）APP自动化测试商户勿…')
    #导航-地址
    address = (MobileBy.ACCESSIBILITY_ID, '四川省,成都市,武侯区中海国际D座1703')
    #导航按钮
    navigation_button = (MobileBy.XPATH,
                         '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[2]/android.view.ViewGroup/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.ScrollView/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout[2]/android.widget.FrameLayout[2]/android.widget.ImageView')
    #导航-取消按钮
    cancel = (MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("取消")')





