from retrying import retry
i = 0
@retry(stop_max_attempt_number=5)
def normal_test():
    global i
    i+=1
    if i == 4:
        print("successful")
    else:
        print(i)
        raise KeyError
if __name__ == '__main__':

    normal_test()