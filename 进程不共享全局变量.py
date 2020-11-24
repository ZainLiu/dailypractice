import multiprocessing
import time

# 定义全局变量
my_list = list()


# 写入数据
def write_data(mylist):
    for i in range(5):
        mylist.append(i)
        time.sleep(0.2)
    print("write_data:", mylist)


# 读取数据
def read_data(mylist):
    print(mylist)


if __name__ == '__main__':
    # 创建写入数据的进程
    write_process = multiprocessing.Process(target=write_data,args=(my_list,))
    read_process = multiprocessing.Process(target=read_data,args=(my_list,))

    write_process.start()
    # 主进程等待写入进程执行完成以后代码 再继续往下执行
    write_process.join()
    read_process.start()