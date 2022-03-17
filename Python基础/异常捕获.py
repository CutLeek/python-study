import logging

LOG_FORMAT = "%(asctime)s [%(levelname)s]  %(message)s"          #配置输出日志格式
DATE_FORMAT = '%Y-%m-%d  %H:%M:%S'                                               #配置输出时间的格式，注意月份和天数不要搞乱了
logging.basicConfig(level=logging.DEBUG,
                    format=LOG_FORMAT,
                    datefmt = DATE_FORMAT ,
                    #filename="/tmp/test.log"                                     #有了filename参数就不会直接输出显示到控制台，而是直接写入文件
                    )


def wrapper(func):
    def try_except(*args,**kwargs):
        try:
            func(*args,**kwargs)
        except Exception as e:
            logging.error(e)
    return try_except

@wrapper
def chu(a,b):
    return a/b

chu(1,0)
print('heiheihei')
