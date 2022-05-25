import pytest

from JiaoZiDT_AppClient_PO.PageObjects.home_page.home_page import HomePage


@pytest.mark.usefixtures("login_app")
# @pytest.mark.home
class TestHome:
    def test_commodity_name_success(self,login_app):
        """
        首页 正确显示商户名称、热度、热度数、商户地址、定位距离、套餐名称【01】
        [Tags]   S
        [Documentation]
        ...    前置条件：
        ...    操作步骤：
        ...    1.使用用户端登录成功
        ...    2.点击首页
        ...    3.查看 商户名称
        ...    4.查看热度
        ...    5.查看热度数
        ...    6.查看商户地址
        ...    7.查看定位距离
        ...    8.查看套餐名称
        ...    预期结果：
        ...    3.商户名称展示正确
        ...    4.商户热度展示正确
        ...    5.商户热度数展示正确
        ...    6.商户地址展示正确
        ...    7.定位距离展示正确
        ...    8.套餐名称展示正确
        """
        #滑动屏幕
        HomePage(login_app).slide_screen_address()
        #判断商户名称
        assert HomePage(login_app).merchants_name() == "（椰云）APP自动化测试商户勿动1111~~"
        #判断热度
        assert HomePage(login_app).heat() == "热度"
        #判断热度数
        assert HomePage(login_app).heat_number() == "4.0"
        #判断商户地址
        assert HomePage(login_app).merchants_address() == "中海国际D座1703"
        #判断定位距离
        assert HomePage(login_app).location() , '329m'
        #套餐名称
        assert HomePage(login_app).setmeal_name()  ,'测试套餐6666###%%%！！！'

    def test_commodity_discount_success(self,login_app):
        """
        首页 正确显示通用饭票字段、爆品折扣字段、饭票折扣字段【02】
        [Tags]   S
        [Documentation]
        ...    前置条件：
        ...    操作步骤：
        ...    1.使用用户端登录成功
        ...    2.点击首页
        ...    3.查看 通用饭票字段展示
        ...    4.查看 爆品折扣字段展示
        ...    5.查看 饭票折扣字段展示
        ...    预期结果：
        ...    3.通用饭票字段展示正确
        ...    4.爆品折扣字段展示正确
        ...    5.饭票折扣字段展示正确
        """
        #滑屏操作
        HomePage(login_app).slide_screen_address()
        #获取“通用饭票”字段
        assert HomePage(login_app).meal() , '通用饭票'
        #获取爆品折扣
        assert HomePage(login_app).explosive_discount() , '5.4折'
        #判断饭票折扣
        assert HomePage(login_app).blue_discount() == "8.8折"

    def test_commodity_price_success(self,login_app):
        """
        首页 正确显示商品副标题、商品购买价格、商品原价【03】
        [Tags]   S
        [Documentation]
        ...    前置条件：
        ...    操作步骤：
        ...    1.使用用户端登录成功
        ...    2.点击首页
        ...    3.查看 商品副标题字段展示
        ...    4.查看 商品购买价格展示
        ...    5.查看 商品原价展示
        ...    预期结果：
        ...    3.商品副标题字段展示正确
        ...    4.商品购买价格展示正确
        ...    5.商品原价展示正确
        """
        #滑屏操作
        HomePage(login_app).slide_screen_title()
        #判断商品副标题
        assert HomePage(login_app).commodity_title() == '测试商品不要动***~~~~'
        #商品购买价格
        assert HomePage(login_app).purchase_price() == '6.67'
        #商品原价
        assert HomePage(login_app).original_price() == '￥12.3'

    def test_location_success(self,login_app):
        """
        首页-导航 正确显示商户名称、商户地址、取消字段【04】
        [Tags]   S
        [Documentation]
        ...    前置条件：
        ...    操作步骤：
        ...    1.使用用户端登录成功
        ...    2.点击首页
        ...    3.查看 导航-商户名称字段展示
        ...    4.查看 导航-商户地址展示
        ...    5.查看 取消字段展示
        ...    预期结果：
        ...    3.导航-商户名称字段展示正确
        ...    4.导航-商户地址展示正确
        ...    5.取消字段展示正确
        """
        #滑屏操作
        HomePage(login_app).slide_screen_address()
        #点击导航按钮
        HomePage(login_app).navigation()
        #获取导航-商户名称
        assert HomePage(login_app).navigation_merchants() ,True
        #获取导航-商户地址
        assert HomePage(login_app).navigation_address() ,True
        #点击去这里按钮
        HomePage(login_app).click_navigation()
        #获取取消按钮
        assert HomePage(login_app).cancel() == '取消'








