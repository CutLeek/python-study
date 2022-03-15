#!/usr/bin/python3

import logging

LOG_FORMAT = "%(asctime)s [%(levelname)s]  %(message)s"          #配置输出日志格式
DATE_FORMAT = '%Y-%m-%d  %H:%M:%S'                                               #配置输出时间的格式，注意月份和天数不要搞乱了
logging.basicConfig(level=logging.DEBUG,
                    format=LOG_FORMAT,
                    datefmt = DATE_FORMAT ,
                    #filename="/tmp/test.log"                                     #有了filename参数就不会直接输出显示到控制台，而是直接写入文件
                    )
logging.debug("debug_msg")
logging.info("info_msg")
logging.warning("warning_msg")
logging.error("error_msg")
logging.critical("critical_msg")
logging.error(LOG_FORMAT)
