import pytest
from JiaoZiDT_AppClient_PO.PageObjects.my_page.my_page import MyPage


@pytest.mark.usefixtures("init_my")
@pytest.mark.my
class TestMy:
    def test_title_success(self,init_my):
        """
        我的 标题、个人信息展示正确【26】
        [Tags]   S
        [Documentation]
        ...    前置条件：
        ...    操作步骤：
        ...    1.使用用户端登录成功
        ...    2.点击我的
        ...    3.查看 用户名称、用户账号、个人中心字段展示
        ...    预期结果：
        ...    3.通用户名称、用户账号、个人中心字段展示正确
        """
        #判断标题
        assert MyPage(init_my).personal_center() == '个人中心'
        #判断用户名称
        assert MyPage(init_my).user_name() == '大胖妹2号'
        #判断用户账号
        assert MyPage(init_my).user_code() == '57929326845'
        #判断通用饭票字段
        assert MyPage(init_my).universal_meal_ticket() == '通用饭票'

    def test_province_detail_success(self,init_my):
        """
        我的页面 成功跳转到省钱页面【27】
        [Tags]   S
        [Documentation]
        ...    前置条件：
        ...    操作步骤：
        ...    1.使用用户端登录成功
        ...    2.点击我的，再次点击省钱
        ...    3.查看 是否跳转到省钱页面
        ...    预期结果：
        ...    3.成功跳转到省钱页面
        """
        #点击进入省钱
        MyPage(init_my).province()
        #判断省钱页面字段
        assert MyPage(init_my).province_detail() == '省钱明细'

    def test_buy_ticket_page_success(self,init_my):
        """
        我的页面 成功跳转到购买饭票页面【28】
        [Tags]   S
        [Documentation]
        ...    前置条件：
        ...    操作步骤：
        ...    1.使用用户端登录成功
        ...    2.点击我的，再次点击购买
        ...    3.查看 是否跳转到饭票页面
        ...    预期结果：
        ...    3.成功跳转到饭票页面
        """
        #点击进入购买饭票页面
        MyPage(init_my).buy_ticket()
        #判断标题
        assert MyPage(init_my).buy_ticket_title() == '购买饭票'
        #判断金额字段
        assert MyPage(init_my).meal_ticket_money() == '1000元'

    def test_meal_ticket_refund(self,init_my):
        """
        我的页面 成功跳转到饭票退款页面【29】
        [Tags]   S
        [Documentation]
        ...    前置条件：
        ...    操作步骤：
        ...    1.使用用户端登录成功
        ...    2.点击我的，再次点击饭票退款
        ...    3.查看 是否跳转到饭票退款页面
        ...    预期结果：
        ...    3.成功跳转到饭票退款页面
        """
        #点击退票按钮
        MyPage(init_my).retrea_ticket()
        #获取标题
        assert MyPage(init_my).meal_ticket_refund() == '饭票退款'
        #点击退款原因
        MyPage(init_my).refund_caus()
        #滑动屏幕
        MyPage(init_my).slide_the_screen_refund()
        #退款按钮
        MyPage(init_my).refund()

    def test_usage_record_success(self,init_my):
        """
        我的页面 成功跳转到饭票退款页面【30】
        [Tags]   S
        [Documentation]
        ...    前置条件：
        ...    操作步骤：
        ...    1.使用用户端登录成功
        ...    2.点击我的，再次点击使用记录
        ...    3.查看 是否跳转到使用记录页面
        ...    预期结果：
        ...    3.成功跳转到使用记录页面
        """
        #点击使用余票
        MyPage(init_my).usage_record()
        #判断标题
        assert MyPage(init_my).transaction_record() == '交易记录'
        #判断当前余票字段
        assert MyPage(init_my).curren_ticket() == '当前余票：'

    def test_red_packet_message_correct(self,init_my):
        """
        我的页面 成功跳转到红包且信息展示正确页面【31】
        [Tags]   S
        [Documentation]
        ...    前置条件：
        ...    操作步骤：
        ...    1.使用用户端登录成功
        ...    2.点击我的，再次点击我的红包，查看红包信息
        ...    3.查看红包信息是否展示正确
        ...    预期结果：
        ...    3.成功跳转到红包页面，信息展示展示正确
        """
        #进入红包
        MyPage(init_my).red_packet()
        #待使用
        assert MyPage(init_my).backlog()  == '待使用'
        #红包名称
        assert MyPage(init_my).red_packet_name() == 'APP自动化测试红包 不要动'
        #有效期
        assert MyPage(init_my).period_of_validity() == '有效期至 2025-05-08'
        #无门槛
        assert MyPage(init_my).no_threshold() == '无门槛'

    def test_detailed_rules_details_success(self,init_my):
        """
        我的页面 红包金额详情展示正确【32】
        [Tags]   S
        [Documentation]
        ...    前置条件：
        ...    操作步骤：
        ...    1.使用用户端登录成功
        ...    2.点击我的，再次点击我的红包，查看红包信息
        ...    3.查看红包金额详情是否展示正确
        ...    预期结果：
        ...    3.红包金额和详情展示正确
        """
        # 进入红包
        MyPage(init_my).red_packet()
        #红包金额
        assert MyPage(init_my).red_packet_money() == '￥5.9'
        #进入详细规则
        MyPage(init_my).detailed_rules()
        #使用规则详情
        assert MyPage(init_my).detailed_rules_details() == 'ui个人个哦如果果然几人io加热偶@#ER￥U&*I（*&……%￥#@#￥%……&*（）8864565'

    def test_red_packet_employ_success(self,init_my):
        """
        我的页面 红包去使用页面跳转成功【33】
        [Tags]   S
        [Documentation]
        ...    前置条件：
        ...    操作步骤：
        ...    1.使用用户端登录成功
        ...    2.点击我的，再次点击我的红包，点击去使用
        ...    3.查看是否跳转到可使用页面
        ...    预期结果：
        ...    3.成功跳转到可使用页面
        """
        # 进入红包
        MyPage(init_my).red_packet()
        #点击去使用
        MyPage(init_my).to_use_the()
        #判断可用商品标题
        assert MyPage(init_my).red_packet_employ() == '可用红包商品'

    def test_have_been_used_red_packet_message_correct(self,init_my):
        """
        我的页面 已使用红包展示正确【34】
        [Tags]   S
        [Documentation]
        ...    前置条件：
        ...    操作步骤：
        ...    1.使用用户端登录成功
        ...    2.点击我的，再次点击我的红包，点击已使用
        ...    3.查看已使用红包信息是否展示正确
        ...    预期结果：
        ...    3.已使用红包信息展示正确
        """
        # 进入红包
        MyPage(init_my).red_packet()
        # 点击已使用
        MyPage(init_my).have_been_used()
        # 红包名称
        assert MyPage(init_my).red_packet_name() == 'APP自动化测试红包 不要动'
        # 无门槛
        assert MyPage(init_my).no_threshold() == '无门槛'
        #判断已过期字段
        assert MyPage(init_my).have_expired() == '已过期'

    def test_have_been_used_jump_success(self,init_my):
        """
        我的页面 已使用红包点击查看跳转到订单页面【35】
        [Tags]   S
        [Documentation]
        ...    前置条件：
        ...    操作步骤：
        ...    1.使用用户端登录成功
        ...    2.点击我的，再次点击我的红包，点击已使用，点击查看
        ...    3.查看是否跳转到订单页面
        ...    预期结果：
        ...    3.成功跳转到订单页面
        """
        # 进入红包
        MyPage(init_my).red_packet()
        # 点击已使用
        MyPage(init_my).have_been_used()
        #点击查看按钮
        MyPage(init_my).examine()
        #跳转成功
        assert MyPage(init_my).commercial_name() == '测试-凉粉饼子'

    def test_collect_message_correct(self,init_my):
        """
        我的页面 成功跳转到我的收藏页面【36】
        [Tags]   S
        [Documentation]
        ...    前置条件：
        ...    操作步骤：
        ...    1.使用用户端登录成功
        ...    2.点击我的，再次点击我的收藏，
        ...    3.查看是否跳转到我的收藏页面
        ...    预期结果：
        ...    3.成功跳转到我的收藏页面
        """
        #点击进入收藏
        MyPage(init_my).my_favorite()
        #判断商品名称
        assert MyPage(init_my).merchant_name() == '九宫格套餐'
        #判断价格
        assert MyPage(init_my).money() == '1'
        #判断标题
        assert MyPage(init_my).title() == '收藏'

    def test_collect_success(self,init_my):
        """
        我的页面 我的收藏页面字段展示正确【37】
        [Tags]   S
        [Documentation]
        ...    前置条件：
        ...    操作步骤：
        ...    1.使用用户端登录成功
        ...    2.点击我的，再次点击我的收藏，
        ...    3.查看我的收藏页面字段展示
        ...    预期结果：
        ...    3.我的收藏页面字段展示正确
        """
        # 点击进入收藏
        MyPage(init_my).my_favorite()
        #点击管理
        MyPage(init_my).management()
        #判断完成
        assert MyPage(init_my).accomplish() == '完成'

    def test_jump_integral_page_success(self,init_my):
        """
        我的页面 交子积分字段展示正确【38】
        [Tags]   S
        [Documentation]
        ...    前置条件：
        ...    操作步骤：
        ...    1.使用用户端登录成功
        ...    2.点击我的，再次点击我的积分，
        ...    3.查看我的积分字段展示
        ...    预期结果：
        ...    3.我的积分页面字段展示正确
        """
        #进入交子积分
        MyPage(init_my).integral_button()
        #获取判断积分余额
        assert MyPage(init_my).integral_balance() == '积分余额：'
        #获取判断标题
        assert MyPage(init_my).integral_text() == '交子积分'

    def test_jump_classify_page_success(self,init_my):
        """
        我的页面 交子积分、收积分码、收积分二维码，展示正确【39】
        [Tags]   S
        [Documentation]
        ...    前置条件：
        ...    操作步骤：
        ...    1.使用用户端登录成功
        ...    2.点击我的，再次点击我的积分，
        ...    3.查看收积分码、收积分二维码展示
        ...    预期结果：
        ...    3.收积分码、收积分二维码展示正确
        """
        #进入交子积分
        MyPage(init_my).integral_button()
        #进入收积分
        MyPage(init_my).collect_integral()
        #判断标题
        assert MyPage(init_my).collect_integral_code() == '收积分码'
        #判断收积分二维码
        assert MyPage(init_my).collect_integral_qr_code() == '收积分二维码'
        #点击立即参与
        MyPage(init_my).participation()
        #判断跳转页面
        assert MyPage(init_my).search() == '搜索'

    def test_transaction_record_jump_success(self,init_my):
        """
        我的页面 交子积分、收积分码、收积分二维码，展示正确【40】
        [Tags]   S
        [Documentation]
        ...    前置条件：
        ...    操作步骤：
        ...    1.使用用户端登录成功
        ...    2.点击我的，再次点击我的积分，
        ...    3.查看收积分码、收积分二维码展示
        ...    预期结果：
        ...    3.收积分码、收积分二维码展示正确
        """
        # 进入交子积分
        MyPage(init_my).integral_button()
        #进入交子记录
        MyPage(init_my).transaction_record_integral_button()
        #判断标题
        assert MyPage(init_my).transaction_record_integral_text() == '交易记录'
        #判断当前积分
        assert MyPage(init_my).current_integral() == '当前积分：'
        #判断交子积分
        assert MyPage(init_my).integral_text() == '交子积分'

    def test_recharge_jump_success(self,init_my):
        """
        我的页面 交子积分、收积分码、收积分二维码，展示正确【42】
        [Tags]   S
        [Documentation]
        ...    前置条件：
        ...    操作步骤：
        ...    1.使用用户端登录成功
        ...    2.点击我的，再次点击我的积分，
        ...    3.查看收积分码、收积分二维码展示
        ...    预期结果：
        ...    3.收积分码、收积分二维码展示正确
        """
        #进入交子积分
        MyPage(init_my).integral_button()
        #进入卡密充值
        MyPage(init_my).integral_recharge()
        #判断标题
        assert MyPage(init_my).password_recharge() == '卡密充值'
        #判断充值
        assert MyPage(init_my).recharge() == '充值'

    def test_jump_binding_success(self,init_my):
        """
        我的页面 交子积分、收积分码、收积分二维码，展示正确【43】
        [Tags]   S
        [Documentation]
        ...    前置条件：
        ...    操作步骤：
        ...    1.使用用户端登录成功
        ...    2.点击我的，再次点击我的积分，
        ...    3.查看收积分码、收积分二维码展示
        ...    预期结果：
        ...    3.收积分码、收积分二维码展示正确
        """
        #进入绑定页面
        MyPage(init_my).binding_phone()
        #判断标题
        # assert MyPage(init_my).binding_phone_mark() == '绑定手机号'
        #判断充值字段
        assert  MyPage(init_my).binding() == '绑定'

    def test_jump_about_us_success(self,init_my):
        """
        我的页面 交子积分、收积分码、收积分二维码，展示正确【44】
        [Tags]   S
        [Documentation]
        ...    前置条件：
        ...    操作步骤：
        ...    1.使用用户端登录成功
        ...    2.点击我的，再次点击我的积分，
        ...    3.查看收积分码、收积分二维码展示
        ...    预期结果：
        ...    3.收积分码、收积分二维码展示正确
        """
        #进入关于我们
        MyPage(init_my).about_us()
        #判断关于交子饭票
        assert MyPage(init_my).about_jiaozi() == '关于交子饭票'
        #判断服务协议
        assert MyPage(init_my).service_agreement() == '服务协议'
        #判断隐私政策
        assert MyPage(init_my).privacy_policy() == '隐私政策'