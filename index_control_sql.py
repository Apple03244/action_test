import mysql.connector as mysql
import json
import os

with open("mysql_info.json","r") as f:
    input = f.read()

# 정속
test=json.loads(input)
test_connect=mysql.connect(**test)
corr=test_connect.cursor()

# 변경가능(index 마지막 값만 불러옴)
corr.execute('''
             use ORIGINAL;
             select id from origin order by id desc limit 1;                          
             ''')
last_index=corr.fetchall()
corr.close()

# 아키텍쳐
index_dict=dict.fromkeys([f"idx_{i}" for i in range(1,21)])
x,y=divmod(last_index,20)
index_list=[range(20*i+1,20*(i+1)+1) for i in range(x)]+[range(20*x,last_index+1)]



# 