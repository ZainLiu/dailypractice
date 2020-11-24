import datetime
def dayofyear():
    year = input("请输入年份:")
    month = input('请输入月份:')
    day = input('请输入天:')
    date1 = datetime.date(year=int(year),month=int(month),day=int(day))
    date2 = datetime.date(year=int(year),month=1,day=1)
    print(type(date1))
    days = (date1 - date2).days + 1
    print('输入的日期是当年的第' + str(days)+ '天')

if __name__ == '__main__':
    dayofyear()