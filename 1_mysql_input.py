import mysql.connector as mc
import json

# Jason 으로 파일 읽기
## 보안 떄문
with open("./mysql_info.json","r") as f:
    inputs=f.read()

    
conneted_corsor=mc.connect()