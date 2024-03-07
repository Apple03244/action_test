# data load(아키텍쳐 생성 예제를 위함)

with open('restaurant_tag_test100.csv',"r") as f:
    test_result=f.readlines()
insert_data=test_result[1:] # 컬럼명 제거

def dropidx(x:str):
    idx_num=x.index(",")
    return x[idx_num+1:]

insert_data=list(map(dropidx,insert_data))

# 가상의 아키텍쳐 생성 코드 -> 크롤링에 맞게 변환 필요

# with open("test_architecture.csv","w") as w:
#     architecture=w.writelines(insert_data)


# 아키텍쳐를 사용하기 위한 환경변수 저장 -> 이 방법이 더 요율적
import os

os.environ["test_architecture_info"]="\n".join(insert_data)