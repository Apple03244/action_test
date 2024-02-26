import csv
import mysql.connector

# MySQL 연결 설정
conn = mysql.connector.connect(
    host="lunch-lab-db.c7gaq8m06dlk.ap-southeast-2.rds.amazonaws.com",
    user="admin",
    password="lunchlab0219",
    database="test"
)
cursor = conn.cursor()

# CSV 파일 경로
csv_file_path = '/Users/ijeonghun/Downloads/restaurant_tag_test100.csv'


# CSV 파일 읽어서 데이터베이스에 삽입
with open(csv_file_path, 'r', encoding='utf-8') as file:
    csv_data = csv.reader(file)
    next(csv_data)  # 헤더 행 스킵
    for row in csv_data:
        
        # tag_test 테이블에 데이터 삽입
        tag_insert_query = '''
        INSERT INTO tag_test (tag, people_cnt)
        VALUES (%s, %s)
        '''
        cursor.execute(tag_insert_query, (row[2], int(row[3])))


        # 매장명 데이터 삽입
        restaurant_insert_query = '''
        INSERT INTO restaurant_test (name)
        VALUES (%s)
        '''
        cursor.execute(restaurant_insert_query, (row[1],))

# 변경사항 커밋
conn.commit()

# 연결 종료
cursor.close()
conn.close()
