import logging
import os
import time

# mylog.py
import logging


#
# class MyLogging():
#     """自定日志之类"""
#     def __init__(self, level):
#         self.level = level
#     def my_log(self):
#
#         # 创建自己的日志收集器
#         my_log = logging.getLogger('DaoSen')
#         my_log.setLevel(self.level.upper())
#         my_log.handlers.clear()
#         # 创建一个日志输出渠道（输出到控制台）
#         handler1 = logging.StreamHandler()
#         handler1.setLevel(self.level.upper())
#         # 创建一个日志输出渠道（输出到文件）
#         now = time.strftime("%Y-%m-%d %H_%M_%S")
#         # screenshot_path = screenshot_dir + "/{}_{}.png".format(img_name, now)
#         handler2 = logging.FileHandler(logs_dir+"/{}.log".format(now), encoding='utf8')
#
#         # handler2 = logging.FileHandler(logs_dir+'.log', encoding='utf8')
#         handler2.setLevel(self.level.upper())
#         # 将输出渠道添加到日志收集器中
#         my_log.addHandler(handler1)
#         my_log.addHandler(handler2)
#
#         # 设置日志输出的格式
#         formatter = '%(asctime)s - [%(filename)s-->line:%(lineno)d] - %(levelname)s: %(message)s'
#         ft1 = logging.Formatter(formatter)
#         # 设置日志输出的格式
#         handler1.setFormatter(ft1)
#         handler2.setFormatter(ft1)
#         return my_log

# #
# # logger = MyLogging('debug').my_log()
# # 此处debug抽出可以使用外部文件配置日志文件输出等级
#
# # if __name__ == '__main__':
# #     logger.debug('爱你2万年')
# #     logger.info('爱你一万年')
# #     logger.warning('爱你一万年')
# #     logger.error('爱你一万年')

import logging

from JiaoZiDT_AppClient_PO.Common.dir_config import logs_dir

now = time.strftime("%Y-%m-%d %H_%M_%S")
def MyLogging(
        name=now,
        # file=now,
        logger_level="DEBUG",
        stream_level="DEBUG",

        file_level="INFO",
        fmt="%(asctime)s-【%(filename)s-->line:%(lineno)d】-%(levelname)s:%(message)s"
):
    # 获取到收集器
    logger = logging.getLogger(name)
    # 设置收集器的级别
    logger.setLevel(logger_level)
    logger.handlers.clear()
    # 输出管理器
    stream_handler = logging.StreamHandler()
    stream_handler.setLevel(stream_level)
    logger.addHandler(stream_handler)
    # 格式
    fmt = logging.Formatter(fmt)
    stream_handler.setFormatter(fmt)
    # if file:
    file_handler = logging.FileHandler(logs_dir+"/{}.log".format(now), encoding='utf8')
    file_handler.setLevel(file_level)
    logger.addHandler(file_handler)
    file_handler.setFormatter(fmt)
    return logger

# if __name__ == "__main__":
#     logger = MyLogging()
#     logger.info("0000")