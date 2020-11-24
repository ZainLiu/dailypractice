import sched
import time


#生成调度器
scheduler = sched.scheduler(time.time, time.sleep)
"""
 一、延迟运行事件
在一个延迟或规定时间之后执行事件，需要采用enter()方法，包含4个参数：
间隔时间(具体值决定与delayfunc, 这里为秒)
优先级(两个事件在同一时间到达的情况)
调用的函数
函数参数
"""

def print_event(name):
    print("EVENT:",time.time(),name)
    # time.sleep(5)


now = time.time()+2
print("START:",time.time())
#分别设置在执行后2秒、3秒之后执行调用函数
scheduler.enterabs(now,3,print_event,('first',))
scheduler.enterabs(now,2,print_event,("second",))
#运行调度器
scheduler.run()
