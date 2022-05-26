""" 订单页面元素 """
from selenium.webdriver.common.by import By


class OrerdManagementLocs:
    #用户账号
    useraccount=(By.XPATH,"//input[@placeholder='请输入用户账号']")
    #用户数据条目
    user_data=(By.XPATH,'//span[@class="el-pagination__total"]')
    #订单号
    order_number=(By.XPATH,"//input[@placeholder='请输入订单号']")
    #订单数据
    # orderdata=(By.XPATH,'//span[@class="el-pagination__total"]')
    #商户名称
    merchant_name=(By.XPATH,"//input[@placeholder='请输入商户名称']")
    # merchantdata=(By.XPATH,"//span[text()='共 7 条']")
    #商品名称
    commodity_name=(By.XPATH,"//input[@placeholder='请输入商品名称']")
    #交易状态
    deal_state=(By.XPATH,'//*[@id="app"]/div/div[2]/section/div/form/div[6]/div/div/div/input')
    #支付成功
    paymentsuccess=(By.XPATH,'//li[@class="el-select-dropdown__item"]//span[text()="支付成功"]')
    #订单创建时间
    order_creation_time=(By.XPATH,'//*[@id="app"]/div/div[2]/section/div/form/div[10]/div/div/input[1]')
    start_time=(By.XPATH,'//div[@class="el-date-range-picker__editor el-input el-input--small"]//input[@placeholder="开始日期"]')
    end_time=(By.XPATH,'//div[@class="el-date-range-picker__editor el-input el-input--small"]//input[@placeholder="结束日期"]')
    start_time1=(By.XPATH,'/html/body/div[2]/div[1]/div/div[2]/table/tbody/tr[4]/td[2]/div/span')
    end_time1=(By.XPATH,"/html/body/div[2]/div[1]/div/div[1]/span[1]/span[2]/div[1]/input")
    click_creation_time=(By.XPATH,"/html/body/div[2]/div[1]/div/div[1]/span[3]/span[2]/div[1]/input")
    #搜索
    search=(By.XPATH,"//span[text()='搜索']")
    #暂无数据
    notdata=(By.XPATH,'//span[text()="暂无数据"]')
    #详细
    detail=(By.XPATH,"//span[text()='详细']")
    #详细信息
    detail_message=(By.XPATH,"//span[text()='订单详情']")
    #翻页功能
    select_page1=(By.XPATH,'//li[text()="4"]')
    #断言翻页功能/输入翻页功能
    get_order=(By.XPATH,"//div[text()='P1501860817337843712124']")
    #输入翻页跳转
    input_page1=(By.XPATH,"//div[@class='el-input el-input--medium el-pagination__editor is-in-pagination'] //input[@class='el-input__inner']")
    #翻页按键
    page_right_key=(By.XPATH,'//i[@class="el-icon el-icon-arrow-right"]')



