import mysql.connector as mysql
import os 

# 크롤링할 primary key 확인 -> index.txt
# 파일 최신화가 필요함

with open('./index.txt',"r") as f:
    indexs=f.read()

# mysql 연동
# 이부분은 각자 입력해야됌
#------------------------------#
config = {
    'user': 'admin',
    'password': 'lunchlab0219',
    'host': "",
    'database': 'test',
    'raise_on_warnings': True
}
#-------------------------------#


# mysql 작동
conn=mysql.connect(**config)

cursor=conn.cursor() # 커서 만들기


# 해야할일 -> 남아있는 매장 index 가져오기
cursor.execute("show tables")
result=cursor.fetchall()
print(result)


# index 파일 최신화 -> 깃 엣션으로 넘어갈 가능성이 있음..






