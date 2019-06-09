import logging

# logging.basicConfig(level=logging.DEBUG,filename=r'mytest.log',format='%(asctime)s %(name)s %(filename)s \
# %(levelname)s  %(message)s',datefmt='%Y-%m-%d %H:%M:%S %a')
# 以上是打印到文件
"""
logging.basicConfig(level=logging.DEBUG,format="%(asctime)s-%(name)s-%(filename)s-%(pathname)s-%(levelname)s : %(message)s",\
                    datefmt="%Y-%m-%d %H:%M:%S %a")
logging.warning("the log is print in the file")
logging.debug("print it to chongle")
#以上是打印到控制台
for i in range(5):
    if i<5:
        logging.debug("this is the %d time print log ",i)
        
"""


class logtest():
    def __init__(self):
        pass

    def log(self):
# 创建一个logger
        logger = logging.getLogger("text")
        logger.setLevel(logging.DEBUG)  # 设置日志的级别
# 创建handl
        fh = logging.FileHandler("textlog.log", encoding="utf-8")  # 将日志输出到textlog.log文件
        ch = logging.StreamHandler()  # 将日志输出到stream
# 设置输出格式
        formatter = logging.Formatter(fmt="%(asctime)s-%(name)s-%(pathname)s-%(filename)s-%(levelname)s : %(message)s", \
                              datefmt="%Y-%m-%d %H:%M:%S %a")
# 为handler制定输出格式

        fh.setFormatter(formatter)
        ch.setFormatter(formatter)

# 为logging添加日志处理器
        logger.addHandler(fh)
        logger.addHandler(ch)
# 输入日志
        #logger.debug("it is a new logtest")
        #logger.debug(u"这个是告警日志")

        return logger
