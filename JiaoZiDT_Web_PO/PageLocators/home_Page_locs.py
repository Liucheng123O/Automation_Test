from selenium.webdriver.common.by import By


class HomePageLocs:
    #业务管理
    business_management=(By.XPATH,"//span[text()='业务管理']")
    #积分溯源
    integral_=(By.XPATH,"//span[text()='积分溯源']")
    #系统管理
    system_management=(By.XPATH,"//span[text()='系统管理']")
    #订单管理
    orerd_management=(By.XPATH,"//span[text()='订单管理']")
    #商户管理
    merchant_management=(By.XPATH,'//*[@id="app"]/div/div[1]/div[2]/div[1]/div/ul/div[5]/li/ul/div[1]/a/li')
    #城市食堂
    city_dining=(By.XPATH,'//span[text()="城市食堂"]')








