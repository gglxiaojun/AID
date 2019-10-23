"""
创建数据dict 使用utf8编码
创建表 words 分为三个字段
id word mean
将dict.txt 中的所有单词存入到数据表中
"""
import pymysql

# 连接数据库
db = pymysql.connect(host='localhost',
                     port=3306,
                     user='root',
                     password='123456',
                     database='dict',
                     charset='utf8')

# 生成游标对象(操作数据库，执行sql语句)
cur = db.cursor()

# 执行对数据的写操作
f = open('dict.txt', 'r')

word_list = []
for i in f:
    word = i.split(' ', 1)[0]
    mean = i.split(' ', 1)[-1]
    word_list.append((word, mean))

    f.close()
sql = "insert into words (word,mean) values (%s,%s)"
try:
    cur.executemany(sql, word_list)
    db.commit()
except Exception as e:
    db.rollback()  # 事务回滚
    print(e)

# 关闭游标和数据库链接
cur.close()
db.close()


def fun():
    print("123起")
    print('你好')
