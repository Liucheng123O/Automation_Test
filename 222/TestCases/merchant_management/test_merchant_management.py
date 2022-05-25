import pytest

from JiaoZiDT_Web_PO.PageObjects.merchant_management_page.merchant_management_page import MerchantManagementPage


@pytest.mark.userfixtures("init_merchant_management")
@pytest.mark.MerchatManagement
class TestMerchatManagement:
    def test_merchantname_search_success(self,init_merchant_management):
        """ 使用 商户名称 搜索成功 """
        #进入商户管理 输入 商户名称
        MerchantManagementPage(init_merchant_management).merchant_name("（测试）甜品店")
        #点击搜索
        MerchantManagementPage(init_merchant_management).search()
        #判断数据
        assert MerchantManagementPage(init_merchant_management).data() == "共 1 条"

    def test_affiliated_unit_search_success(self,init_merchant_management):
        """ 使用 所属商务名称 搜索成功 """
        #输入 所属商务名称
        MerchantManagementPage(init_merchant_management).affiliated_unit("小王")
        #点击搜索
        MerchantManagementPage(init_merchant_management).search()
        #判断条数
        assert MerchantManagementPage(init_merchant_management).data() == "共 1 条"

    def test_contacts_name_search_success(self,init_merchant_management):
        """ 使用 联系人姓名 搜索成功 """
        #输入联系人姓名
        MerchantManagementPage(init_merchant_management).contacts_name("刘")
        #点击搜索
        MerchantManagementPage(init_merchant_management).search()
        #判断
        assert MerchantManagementPage(init_merchant_management).data() == "共 1 条"

    def test_contacts_phone_search_success(self,init_merchant_management):
        """ 使用 电话号码 搜索成功 """
        #输入 电话号码查询
        MerchantManagementPage(init_merchant_management).contacts_phone("17608001572")
        #点击所搜
        MerchantManagementPage(init_merchant_management).search()
        #判断
        assert MerchantManagementPage(init_merchant_management).data() == "共 1 条"

    def test_open_state_search_success(self,init_merchant_management):
        """ 状态 选择显示搜索成功 """
        # 选择状态
        MerchantManagementPage(init_merchant_management).state()
        # 输入 电话号码查询
        MerchantManagementPage(init_merchant_management).contacts_phone("17608001572")
        #点击搜索
        MerchantManagementPage(init_merchant_management).search()
        #判断
        assert MerchantManagementPage(init_merchant_management).data() == "共 1 条"

    def test_business_search_success(self,init_merchant_management):
        """ 商圈 选择悠方搜索成功 """
        #点击选择 商圈  悠方
        MerchantManagementPage(init_merchant_management).business_youfang()
        # 输入联系人姓名
        MerchantManagementPage(init_merchant_management).contacts_name("刘")
        #点击搜索
        MerchantManagementPage(init_merchant_management).search()
        #判断
        assert MerchantManagementPage(init_merchant_management).data() == "共 1 条"

    def test_mixture_search_success(self,init_merchant_management):
        """ 混合搜索 商户名称、联系人姓名、状态、商圈 """
        #  输入 商户名称
        MerchantManagementPage(init_merchant_management).merchant_name("（测试）快乐奶茶")
        # 输入联系人姓名
        MerchantManagementPage(init_merchant_management).contacts_name("刘")
        # 选择状态
        MerchantManagementPage(init_merchant_management).state()
        # 点击选择 商圈  悠方
        MerchantManagementPage(init_merchant_management).business_youfang()
        #点击搜索
        MerchantManagementPage(init_merchant_management).search()
        # 判断
        assert MerchantManagementPage(init_merchant_management).data() == "共 1 条"

    def test_state_close_open_success(self,init_merchant_management):
        """ 开启 关闭商户成功 """
        #  输入 商户名称
        MerchantManagementPage(init_merchant_management).merchant_name("（测试）快乐奶茶")
        # 输入联系人姓名
        MerchantManagementPage(init_merchant_management).contacts_name("刘")
        # 选择状态
        MerchantManagementPage(init_merchant_management).state()
        # 点击选择 商圈  悠方
        MerchantManagementPage(init_merchant_management).business_youfang()
        # 点击搜索
        MerchantManagementPage(init_merchant_management).search()
        #关闭状态
        MerchantManagementPage(init_merchant_management).state_open_close()
        # 再次点击搜索
        MerchantManagementPage(init_merchant_management).search()
        #判断是否开启
        assert MerchantManagementPage(init_merchant_management).not_data() == "暂无数据"
        # 选择状态
        MerchantManagementPage(init_merchant_management).state1()
        # 点击搜索
        MerchantManagementPage(init_merchant_management).search()
        # 开启状态
        MerchantManagementPage(init_merchant_management).state_open_close()
        # 选择状态
        MerchantManagementPage(init_merchant_management).state()
        # 点击搜索
        MerchantManagementPage(init_merchant_management).search()
        # 判断是否开启
        assert MerchantManagementPage(init_merchant_management).data() == "共 1 条"

    def test_change_sava_success(self,init_merchant_management):
        """ 商户管理 修改保存成功 """
        # 输入id
        MerchantManagementPage(init_merchant_management).id("6")
        # 搜索
        MerchantManagementPage(init_merchant_management).search()
        #进入修改
        MerchantManagementPage(init_merchant_management).change_save()
        #判断 是否成功
        assert MerchantManagementPage(init_merchant_management).save_hint() == "保存成功！"

    def test_id_search_success(self,init_merchant_management):
        """ 商户管理 通过id 可成功搜索 """
        #输入id
        MerchantManagementPage(init_merchant_management).id("6")
        #搜索
        MerchantManagementPage(init_merchant_management).search()
        #判断
        assert MerchantManagementPage(init_merchant_management).data() == "共 1 条"

    def test_recharge_integra_success(self,init_merchant_management):
        """ 商户管理 积分充值成功"""
        # 输入id
        MerchantManagementPage(init_merchant_management).id("6")
        # 搜索
        MerchantManagementPage(init_merchant_management).search()
        #输入积分  判断
        assert MerchantManagementPage(init_merchant_management).integra_money(10) == 10

    def test_freeze_success(self,init_merchant_management):
        """ 商户管理  积分冻结成功 """
        # 输入id
        MerchantManagementPage(init_merchant_management).id("6")
        # 搜索
        MerchantManagementPage(init_merchant_management).search()
        #解冻积分判断
        assert MerchantManagementPage(init_merchant_management).freeze_money(10)  == 10

    def test_unfreeze_success(self,init_merchant_management):
        """ 商户管理  积分解冻成功"""
        # 输入id
        MerchantManagementPage(init_merchant_management).id("6")
        # 搜索
        MerchantManagementPage(init_merchant_management).search()
        #解冻积分判断
        assert MerchantManagementPage(init_merchant_management).unfreeze(10)  == 10

    # @pytest.mark.MerchatManagement
    def test_add_staff_success(self,init_merchant_management):
        """ 商户管理  添加员工成功  """
        # 输入id
        MerchantManagementPage(init_merchant_management).id("6")
        # 搜索
        MerchantManagementPage(init_merchant_management).search()
        #进入员工管理
        MerchantManagementPage(init_merchant_management).staff_management()
        #添加
        MerchantManagementPage(init_merchant_management).add_staff("17608011575","六六六")
        #判断
        assert MerchantManagementPage(init_merchant_management).judge_name() == "六六六"
        #删除
        MerchantManagementPage(init_merchant_management).delete()

    def test_change_success(self,init_merchant_management):
        """ 商户管理  修改员工成功  """
        # 输入id
        MerchantManagementPage(init_merchant_management).id("6")
        # 搜索
        MerchantManagementPage(init_merchant_management).search()
        # 进入员工管理
        MerchantManagementPage(init_merchant_management).staff_management()
        # 添加
        MerchantManagementPage(init_merchant_management).add_staff("17608011573", "六六六")
        #修改
        MerchantManagementPage(init_merchant_management).change("七七七")
        # 判断
        assert MerchantManagementPage(init_merchant_management).change_name() == "六六六七七七"
        # 删除
        MerchantManagementPage(init_merchant_management).delete()















