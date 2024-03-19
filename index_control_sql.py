import mysql.connector as mysql
import json
import os

with open("mysql_info.json","r") as f:
    input = f.read()

# 정속
test=json.loads(input)
test_connect=mysql.connect(**test)
corr=test_connect.cursor()

#변경가능(index 마지막 값만 불러옴)
corr.execute('''
             use ORIGINAL;
             select id from origin order by id desc limit 1;                          
             ''')
last_index=corr.fetchall()
corr.close()

# 아키텍쳐
index_dict={}
temp=last_index/20
for i in range(20):
    index_dict[i]=