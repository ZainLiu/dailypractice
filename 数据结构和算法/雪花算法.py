import time

class MySnow(object):
    def __init__(self, dataID):
        self.start = int(time.mktime(time.strptime("2018-01-01 00:00:00", "&Y-%m-%d %H:%M:%S")))
        self.last = int(time.time())
        self.countID = 0
        self.dataID = dataID

    def get_id(self):
        now = int(time.time())
        temp = now-self.start
        if len(str(temp)) < 9:  # 时间差不够9位在前面补0
            length = len(str(temp))
            s = "0"*(9-length)
            temp = s + str(temp)
            # temp = "%09d"%temp
        if now == self.last:
            self.countID += 1
        else:
            self.countID = 0
            self.last = now
        # 标识ID部分
        if len(str(self.dataID)) < 2:
            length = len(str(self.dataID))
            s = "0" * (2-length)
            self.dataID = s + str(self.dataID)
        # 自增序列号部分
        if self.countID == 99999:  # 序列号自增满5位，睡眠一分钟
            time.sleep(1)
        coutIDdata = str(self.countID)
        if len(coutIDdata) < 5:
            length = len(coutIDdata)
            s = "0" * (5 - length)
            count = s + coutIDdata
        id = str(temp) + str(self.dataID) + coutIDdata
        return id

