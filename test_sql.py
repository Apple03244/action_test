import mysql.connector as mysql
import json

with open("test_json.json","r") as f:
    input = f.read()

test=json.loads(input)
test_connect=mysql.connect(**test)
corr=test_connect.cursor()
corr.execute("show databases")