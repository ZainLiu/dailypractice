import threading


# 定义全局变量
g_num = 0

# 创建全局互斥锁
lock = threading.Lock()


# 循环一次给全局变量加1
def sum_num1():
    # 上锁

    for i in range(1000000):
        global g_num
        lock.acquire()
        g_num += 1
        if i ==10086:
            b = 1/0
        lock.release()

    print("sum1:", g_num)
    # 释放锁



# 循环一次给全局变量加1
def sum_num2():
    # 上锁

    for i in range(1000000):
        global g_num
        # lock.acquire()
        g_num += 1
        # lock.release()
    print("sum2:", g_num)
    # 释放锁



if __name__ == '__main__':
    # 创建两个线程
    first_thread = threading.Thread(target=sum_num1)
    second_thread = threading.Thread(target=sum_num2)
    # 启动线程
    first_thread.start()
    second_thread.start()
