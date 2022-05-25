from selenium.webdriver.common.by import By


class LoinPageLocs:
    # 用户名输入框
    user_input = (By.XPATH, '//input[@placeholder="账号"]')
    # 密码输入框
    pass_input = (By.XPATH, '//input[@placeholder="密码"]')
    # 点击登录
    login_button = (By.XPATH, '//button[@type="button"]')
    # 登录表单区域的提示信息框
    msg_from_login_user = (By.XPATH, '//*[@id="app"]/div/form/div[1]/div/div[2]')
    msg_from_login_password = (By.XPATH, '//*[@id="app"]/div/form/div[1]/div/div[2]')
    # 验证码
    auth_code = (By.XPATH, '//input[@placeholder="验证码"]')
    # 错误提示语
    marked_words = (By.XPATH, "/html/body/div[2]")
    home = (By.XPATH, '//span[text()="首页"]')
    #打开列表
    open_list=(By.XPATH,"//div[@id='hamburger-container']")
