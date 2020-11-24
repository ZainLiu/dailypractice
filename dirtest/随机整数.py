import random
start_num = int(input("起始楼层："))
end_num = int(input("结束楼层："))
luck_num = random.randint(start_num,end_num)
print("幸运楼层是：%s"%luck_num)
