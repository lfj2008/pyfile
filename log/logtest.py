from log import logtest

class test():
    def __init__(self):
        self.log = logtest().log()

    def print_log(self):
        self.log.info("print a test about log")

if __name__=="__main__":
    t = test()
    t.print_log()