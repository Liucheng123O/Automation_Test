from selenium.webdriver.common.by import By


class EnterpriseManagementlocs:
    #企业管理
    enterprise_management=(By.XPATH,'//span[text()="企业管理"]')
    #新增
    add_city=(By.XPATH,'//span[text()="新增"]')
    #企业名称
    add_enterprise_name=(By.XPATH,'//*[@id="app"]/div/div[2]/section/div/form/div[1]/div/div[1]/input')
    #企业地址
    add_enterprise_address=(By.XPATH,'//*[@id="app"]/div/div[2]/section/div/form/div[2]/div/div/input')
    #法人姓名
    add_legal_person_name=(By.XPATH,'//*[@id="app"]/div/div[2]/section/div/form/div[5]/div/div/input')
    # 营业执照
    add_business_license=(By.XPATH,'//*[@id="app"]/div/div[2]/section/div/form/div[7]/div/div/div[1]/div')
    #身份证
    add_id_number1=(By.XPATH,'//*[@id="app"]/div/div[2]/section/div/form/div[8]/div[1]/div/div/div[1]/div')
    add_id_number2=(By.XPATH,'//*[@id="app"]/div/div[2]/section/div/form/div[8]/div[2]/div/div/div[1]/div')
    #立即创建
    add_creat=(By.XPATH,'//span[text()="立即创建"]')
    #开户行
    opening_bank=(By.XPATH,'//*[@id="app"]/div/div[2]/section/div/form/div[9]/div/div/input')
    #银行卡
    bank_card=(By.XPATH,'//*[@id="app"]/div/div[2]/section/div/form/div[10]/div/div/input')
    #企业名称
    enterprise_name=(By.XPATH,'//input[@placeholder="请输入商户名称"]')
    #数据总数 ，共一条
    data=(By.XPATH,'//span[text()="共 1 条"]')
    #搜索
    search=(By.XPATH,'//span[text()="搜索"]')
    #充值按钮
    recharge_button=(By.XPATH,'//*[@id="app"]/div/div[2]/section/div/div[2]/div[3]/table/tbody/tr/td[12]/div/button[2]/span')
    #金额
    recharge_amount=(By.XPATH,'/html/body/div[2]/div/div[2]/form/div[1]/div/div/div/input')
    # 确定按钮
    recharge_confirm=(By.XPATH,'//span[text()="确 定"]')
    #获取金额
    get_amount=(By.XPATH,'//*[@id="app"]/div/div[2]/section/div/div[2]/div[3]/table/tbody/tr/td[6]/div')
    #冻结
    freeze_button=(By.XPATH,'//*[@id="app"]/div/div[2]/section/div/div[2]/div[3]/table/tbody/tr/td[12]/div/button[3]/span')
    #输入冻结金额
    freeze_amount=(By.XPATH,'/html/body/div[2]/div/div[2]/form/div[1]/div/div/div/input')
    #获取冻结金额
    get_freeze_amount=(By.XPATH,'//*[@id="app"]/div/div[2]/section/div/div[2]/div[3]/table/tbody/tr/td[7]/div')
    #解冻
    unfreeze_button=(By.XPATH,'//*[@id="app"]/div/div[2]/section/div/div[2]/div[3]/table/tbody/tr/td[12]/div/button[4]/span')
    #获取解冻金额
    get_unfreeze=(By.XPATH,'')
    #编辑
    edit_button=(By.XPATH,'')



