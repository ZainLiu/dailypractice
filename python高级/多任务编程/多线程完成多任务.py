import threading
import time


def sing():
    # print('sing当前执行的线程为：', threading.current_thread())
    for i in range(6):
        print(f'正在唱歌{i}')
        time.sleep(1)


def dance():
    # print('dance当前执行的线程为：', threading.current_thread())
    for i in range(6):
        print(f'正在跳舞{i}')
        time.sleep(1)


if __name__ == '__main__':
    sing_thread = threading.Thread(target=sing)
    dance_thread = threading.Thread(target=dance)

    sing_thread.start()
    dance_thread.start()
