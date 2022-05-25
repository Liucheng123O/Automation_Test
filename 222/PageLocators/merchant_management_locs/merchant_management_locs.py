from selenium.webdriver.common.by import By


class MerchantManagementLocs:
    #商户名称
    merchanr_name=(By.XPATH,"//input[@placeholder='请输入商户名称']")
    #所属商务
    affiliated_unit=(By.XPATH,"//input[@placeholder='请输入商务名称']")
    #联系人姓名
    contacts_name=(By.XPATH,"//input[@placeholder='请输入联系人姓名']")
    #联系电话
    contacts_phone=(By.XPATH,"//input[@placeholder='请输入联系人电话']")
    #状态
    state1=(By.XPATH,'//*[@id="app"]/div/div[2]/section/div/form/div[6]/div/div/div/input')
    state2=(By.XPATH,"//span[text()='显示']")
    state3=(By.XPATH,"//span[text()='隐藏']")
    #商圈
    business=(By.XPATH,"//input[@placeholder='--选择商圈--']")
    #商圈-悠方
    business_youfang=(By.XPATH,"//span[text()='悠方']")
    #搜索
    search=(By.XPATH,"//span[text()='搜索']")
    #数据条数
    data=(By.XPATH,"//span[@class='el-pagination__total']")
    #状态 打开/关闭
    state_open_close=(By.XPATH,'//*[@id="app"]/div/div[2]/section/div/div[2]/div[3]/table/tbody/tr/td[18]/div/div/span')
    #关闭后 点击 确定
    click_open_close=(By.XPATH,"//button[@class='el-button el-button--default el-button--small el-button--primary ']")
    #暂无数据 断言
    not_data=(By.XPATH,'//span[text()="暂无数据"]')
    #id 搜索
    id=(By.XPATH,'//input[@placeholder="请输入ID"]')
    #修改
    changed=(By.XPATH,'//*[@id="app"]/div/div[2]/section/div/div[2]/div[3]/table/tbody/tr/td[20]/div/button[1]/span')
    #确定保存
    save_click=(By.XPATH,'//span[text()="确定保存"]')
    #保存成功 提示语
    save_hint=(By.XPATH,'//p[text()="保存成功！"]')
    #充值按钮
    recharge_button=(By.XPATH,'//*[@id="app"]/div/div[2]/section/div/div[2]/div[3]/table/tbody/tr/td[20]/div/button[2]/span')
    #输入积分数目
    recharge_integral=(By.XPATH,'//input[@placeholder="请输入积分数量"]')
    #确定
    recharge_click_buuton=(By.XPATH,'/html/body/div[2]/div/div[3]/div/button[1]')
    #冻结
    freeze=(By.XPATH,'//span[text()="冻结"]')
    freeze1=(By.XPATH,'//*[@id="app"]/div/div[2]/section/div/div[2]/div[3]/table/tbody/tr/td[12]')
    #输入冻结金额
    input_freeze_money=(By.XPATH,"//input[@placeholder='请输入积分数量']")
    #冻结中的确定
    freeze_click=(By.XPATH,"/html/body/div[5]/div/div[3]/div/button[1]")
    #解冻
    unfreeze=(By.XPATH,'//span[text()="解冻"]')
    #输入解冻金额
    input_unfreeze_money=(By.XPATH,'//input[@placeholder="请输入积分数量"]')
    #解冻确认
    click_unfreeze=(By.XPATH,"/html/body/div[7]/div/div[2]/form/div[1]/div/div/input")
    #获取积分数
    get_integral=(By.XPATH,'//*[@id="app"]/div/div[2]/section/div/div[2]/div[3]/table/tbody/tr/td[11]/div')
    #员工管理
    staff_management=(By.XPATH,'//*[@id="app"]/div/div[2]/section/div/div[2]/div[3]/table/tbody/tr/td[20]/div/button[5]/span')
    #添加员工
    add_staff=(By.XPATH,'//*[@id="app"]/div/div[2]/section/div/div[1]/div[1]')
    #电话
    add_phone=(By.XPATH,'//input[@placeholder="请输入手机号码"]')
    #姓名
    add_name=(By.XPATH,'//div[@class="el-input el-input--medium"]//input[@placeholder="请输入姓名"]')
    #确定
    add_button=(By.XPATH,'//span[text()="确 定"]')
    #判断数据
    judge_name=(By.XPATH,'//div[text()="六六六"]')
    #修改判断
    change_name=(By.XPATH,'//div[text()="六六六七七七"]')
    #删除
    delete=(By.XPATH,'//*[@id="app"]/div/div[2]/section/div/div[2]/div[3]/table/tbody/tr/td[6]/div/button[2]/span')
    #删除确定
    delete_button=(By.XPATH,'/html/body/div[4]/div/div[3]/button[2]/span')
    #修改
    change=(By.XPATH,'//*[@id="app"]/div/div[2]/section/div/div[2]/div[3]/table/tbody/tr/td[6]/div/button[1]/span')
















