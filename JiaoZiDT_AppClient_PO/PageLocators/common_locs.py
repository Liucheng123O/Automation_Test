from appium.webdriver.common.mobileby import MobileBy


class CommonLocs:
    # 首页
    home = (MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("首页")')
    # 分类
    classify = (MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("分类")')
    # 我的饭票
    my_meal = (MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("我的饭票")')
    # 我的
    my = (MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("我的")')
    # 搜索
    search = (MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("搜索")')
    # 弹窗 关闭按钮
    close_windows = (MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("交子饭票")')
