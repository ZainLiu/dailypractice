from pymysql import connect

db = connect(host='192.168.40.131', port=3306, database='test', user='root', password='mysql', charset='utf8')
cur = db.cursor()
