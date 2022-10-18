from MySQLdb import connect
from MySQLdb import OperationalError
try:
# 연결
    db = connect(user='webdb',password='webdb',host='127.0.0.1', port=3306, db='webdb', charset='utf8')

    # cursor 생성
    cursor = db.cursor()

    # sql(insert문)실행

    sql = 'insert into pet value("성성이","홍길동","dog","m","2016-12-23",null)'
    count =  cursor.execute(sql)
#   commit
    db.commit()


#     자원 정리
    cursor.close()
    db.close()
#   결과 확인


    print(f'실행결과: {"성공"if count == 1 else "실패"}')

except OperationalError as e:
    print(f'에러:{e}')