"""

根据标签收集用例并运行

"""
import pytest
#           #标签 执行哪些用例
# pytest.main(["-s","-v","-m","demo",
#              #测试报告路径
#              "--html=Outputs/reports/report.html",
#              #重运行
#              "--reruns-delay","5",
#             # 生成allure测试报告
#             "--alluredir=Outputs/allure_reports",
#             #重运行
#              "--reruns","2","--reruns-delay","5"])

# D:\pycharm\JiaoZiDT_Web_PO
# allure serve Outputs/allure_reports
#
pytest.main(["-s","-v","-m","CommodityManagement",
             #测试报告路径
             "--html=Outputs/reports/report.html",
             "--alluredir=Outputs/allure_reports",
             ])

#与直接运行是一样的,加上参数之后可以自定义运行
# pytest.main(["-s","-v","-m","order",
#              "--reruns","1","--reruns-delay","5"])
# pytest.main(["-s","-v","-m","debug"])
# 全部运行
# pytest.main(["--html=Outputs/reports/report.html",
#              "--reruns","2","--reruns-delay","5",
#              # "--alluredir=Outputs/allure_reports"
#              ])
# #运行整个包下面的
# pytest.main("-s","-v","95pytest","debug")

