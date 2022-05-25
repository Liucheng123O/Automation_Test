import pytest
# #
# pytest.main(["-s","-v","-m","my ",
#
#              #测试报告路径
#
#
#              ])

#
# 全部运行
pytest.main(["--html=Outputs/reports/report.html",
             "--reruns","1","--reruns-delay","5",
             "--alluredir=Outputs/allure_reports"
             ])







