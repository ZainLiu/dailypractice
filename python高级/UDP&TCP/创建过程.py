
import multiprocessing
def sing():
    pass
if __name__ == '__main__':
    # 创建进程池，3表示进程池容量
    pool=multiprocessing.Pool(3)
    for i in range(5):
        pass
        # pool.apply(sing)# 进程池里的进程同步处理
        pool.apply_async(sing)#进程池里的进程异步处理
    #封闭进程池, 意思告诉主进程以后不会有新的任务添加进来（异步处理才要加）
    pool.close()
    #主进程等待进程池执行完成以后程序再退出(异步处理才要加)
    pool.join()


