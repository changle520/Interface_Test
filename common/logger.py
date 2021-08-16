import logging
import time
import os
import sys
from common.utils import mkdir


class Logging:
    """setup logging

        Examples:
            >>> import logging
            >>> Logging()
            >>> logging.debug("this is debug message")

            /log/2020-11-24.log

                [2020-11-24 16:22:13,711]  [logger.py : 94] [ERROR] - this is debug message
        """

    def __init__(self):
        """ settings logging
        """
        """
            第一步，初始化 log 目录
        """
        day_time = time.strftime('%Y-%m-%d', time.localtime(time.time()))  # 2020-04-20
        minutes_time = time.strftime('%Y-%m-%d-%H-%M', time.localtime(time.time()))  # 2020-04-20

        path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # 项目路径

        log_folder = "{}/log".format(path)
        log_child_folder = "{}/log/{}".format(path, day_time)

        mkdir(log_folder)
        log_file = "{}/{}.log".format(log_folder, day_time)
        #log_file = "{}/{}.log".format(log_folder, minutes_time)
        """
            第二步，创建一个handler，用于写入全部info日志文件
        """
        # a 代表继续写log，不覆盖之前log
        # w 代表重新写入，覆盖之前log
        file_handler = logging.FileHandler(log_file, mode='a+',encoding="UTF-8")
        file_handler.setLevel(logging.DEBUG)

        """
            第三步，创建一个handler，用于写入错误日志文件
        """
        # 由于 error log 文件只写入错误行内容，已经在log文件内覆盖，所以没必要
        # error_file_handler = logging.FileHandler(log_err_file, mode='a+')
        # error_file_handler.setLevel(logging.ERROR)

        """
            第四步，再创建一个handler，用于输出到控制台
        """
        stdout_handler = logging.StreamHandler(sys.stdout)
        stdout_handler.setLevel(logging.DEBUG)

        """
            第五步，定义handler的输出格式
        """
        # formatter = logging.Formatter(
        #     "[%(levelname)s - %(asctime)s - %(filename)s] : %(message)s"
        # )
        #- [line: %(lineno)s]
        formatter = logging.Formatter(
            "[%(asctime)s]  [%(filename)s : %(lineno)s] [%(levelname)s] - %(message)s"
        )


        file_handler.setFormatter(formatter)
        # error_file_handler.setFormatter(formatter)
        stdout_handler.setFormatter(formatter)

        """
            第六步，将logger添加到handler里面
        """
        logger = logging.getLogger()
        logger.setLevel(logging.DEBUG)
        logger.handlers = []

        logger.addHandler(file_handler)
        # logger.addHandler(error_file_handler)
        logger.addHandler(stdout_handler)


if __name__ == '__main__':
    Logging()
    logging.debug("this is debug debug")
    logging.error("this is debug error")
