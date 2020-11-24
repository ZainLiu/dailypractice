import time,random

def generate_order_sn():
    t = time.time()
    code = int(t * 1000000)
    rand = random.randint(10000, 99999)
    return 'SN'+str(code)+str(rand)
if __name__ == '__main__':
    print(generate_order_sn())
