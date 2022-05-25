from selenium.webdriver.common.by import By


class CommodityManagementLocs:
    #商品管理
    commoditymanagement=(By.XPATH,'//span[text()="商品管理"]')
    commoditymanagement1=(By.XPATH,'//li[@class="el-menu-item is-active"]//span[text()="商品管理"]')
    #新增
    add_management=(By.XPATH,"//span[text()='新增']")
    #套餐所属商户
    affiliated_merchants=(By.XPATH,'//input[@placeholder="请输入套餐所属商户"]')
    #点击商品
    click_commodity = (By.XPATH, '/html/body/div[2]/div[1]/div[1]/ul/li[1]/span')
    #商品库存数量
    quantity_instock=(By.XPATH,'//div[@class="el-form-item__content"]//div[@class="el-input el-input--medium"]//input[@class="el-input__inner"]')
    #排序
    #商品标题
    commodity_title = (By.XPATH,'//input[@placeholder="请输入商品标题"]')
    #优惠商品图片
    uploading_picture=(By.XPATH,'//*[@id="app"]/div/div[2]/section/div/form/div[2]/div[2]/div[3]/div/div[2]/div/div/div')
    #套餐名称
    set_name=(By.XPATH,'//*[@id="app"]/div/div[2]/section/div/form/div[2]/div[1]/div[4]/div/div/input')
    #商品套餐副标题
    subheading=(By.XPATH,'//*[@id="app"]/div/div[2]/section/div/form/div[2]/div[1]/div[5]/div/div/input')
    #商品一级分类
    classification1=(By.XPATH,'//*[@id="app"]/div/div[2]/section/div/form/div[2]/div[1]/div[6]/div/div/div[1]/input')
    click_classification1=(By.XPATH,"/html/body/div[3]/div[1]/div[1]/ul/li[1]/span")
    #商品二级分类
    classification2=(By.XPATH,'//*[@id="app"]/div/div[2]/section/div/form/div[2]/div[1]/div[7]/div/div/div[1]/input')
    click_classification2=(By.XPATH,"//span[text()='快餐简餐']")
    #包含单品
    include_solo=(By.XPATH,'//*[@id="app"]/div/div[2]/section/div/form/div[3]/div[1]/div/div[1]/input')
    #单品价格
    solo_price=(By.XPATH,'//*[@id="app"]/div/div[2]/section/div/form/div[3]/div[2]/div/div[1]/div/input')
    #门店价格
    shop_price=(By.XPATH,'//*[@id="app"]/div/div[2]/section/div/form/div[7]/div/div/div/input')
    #帮抢价格
    help_price=(By.XPATH,'//*[@id="app"]/div/div[2]/section/div/form/div[8]/div/div/div/input')
    #使用规则
    service_regulations=(By.XPATH,'//*[@id="app"]/div/div[2]/section/div/form/div[12]/div[2]/div/div/div/textarea')
    #单买价格
    price=(By.XPATH,'//*[@id="app"]/div/div[2]/section/div/form/div[9]/div/div/div/input')
    #商家底价
    floor_price=(By.XPATH,'//*[@id="app"]/div/div[2]/section/div/form/div[10]/div/div/div/input')
    #点击可用时间
    start_data_1=(By.XPATH,'//*[@id="app"]/div/div[2]/section/div/form/div[12]/div[1]/div[1]/div/div[1]/input[1]')
    #开始日期
    start_data=(By.XPATH,'/html/body/div[5]/div[1]/div/div[1]/table/tbody/tr[2]/td[4]')
    #结束日期
    date_closed=(By.XPATH,'/html/body/div[5]/div[1]/div/div[2]/table/tbody/tr[6]/td[2]')
    #点击开始时间
    start_time_1=(By.XPATH,'//*[@id="app"]/div/div[2]/section/div/form/div[12]/div[1]/div[2]/div/div/input[1]')
    #开始时间
    start_time=(By.XPATH,'/html/body/div[3]/div[1]/div[1]/div[2]/div/div[1]/div[1]/ul/li[1]')
    #结束时间
    time_closed=(By.XPATH,'/html/body/div[3]/div[1]/div[2]/div[2]/div/div[1]/div[1]/ul/li[24]')
    #确定
    confirm=(By.XPATH,'//button[text()="确定"]')
    #立即创建
    immediately_create=(By.XPATH,'//span[text()="立即创建"]')
    #判断是否创建成功
    create_successful=(By.XPATH,'//p[text()="创建成功"]')
    #商户名称
    commercial_name0=(By.XPATH,'//input[@placeholder="请输入商户名称 "]')
    #商品名称
    commodity_name=(By.XPATH,'//input[@placeholder="请输入商品名称"]')
    #排序
    sort1=(By.XPATH,'//*[@id="app"]/div/div[2]/section/div/form/div[4]/div/div[1]/input')
    sort2=(By.XPATH,'//*[@id="app"]/div/div[2]/section/div/form/div[4]/div/div[2]/input')
    #搜索
    search=(By.XPATH,'//*[@id="app"]/div/div[2]/section/div/form/div[12]/div/button[1]')
    #商品 数据数量
    commodity_quantity=(By.XPATH,'//*[@id="app"]/div/div[2]/section/div/div[2]/div[2]/div/span[1]')
    #判断是否存在数据
    no_data=(By.XPATH,'//span[text()="暂无数据"]')
    #编辑
    editor=(By.XPATH,'//span[text()="编辑"]')
    #保存
    commodity_sava=(By.XPATH,'//span[text()="保存"]')
    #保存提示语
    sava_hint=(By.XPATH,"//p[@class='el-message__content']")
    #商品类型
    click_commodity_type=(By.XPATH,"//input[@placeholder='--选择品类--']")
    #选择汽车服务
    click_server0=(By.XPATH,"/html/body/div[2]/div[1]/div[1]/ul/li[9]")
    #
    click_commodity_type1=(By.XPATH,"//input[@placeholder='--选择二级品类--']")
    click_server1=(By.XPATH,"//span[text()='其他']")

    #上下架商品
    commodity_open=(By.XPATH,"//div[@class='el-switch is-checked']")
    commodity_close=(By.XPATH,"//div[@class='el-switch']")
    #上下架提示语
    close_open_hint=(By.XPATH,'//p[text()="修改成功"]')
















