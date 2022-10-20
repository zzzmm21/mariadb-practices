from MySQLdb import connect, OperationalError
from MySQLdb.cursors import DictCursor

def findall():
    try:
        db = connect(
            user='bookmall',
            password='bookmall',
            host='127.0.0.1',
            port=3306,
            db='bookmall',
            charset='utf8')
        cursor = db.cursor(DictCursor)

        sql = 'select mem_name as 회원이름, tel as 전화번호, email , password from member'
        cursor.execute(sql)

        results = cursor.fetchall()

        cursor.close()
        db.close()


        print('member 리스트 가져오기')

        return results
    except OperationalError as e:
        print(f'에러: {e}')

def insert():
    try:
    # 연결
        db = connect(user='bookmall',password='bookmall',host='127.0.0.1', port=3306, db='bookmall', charset='utf8')

        # cursor 생성
        cursor = db.cursor()

        # sql(insert문)실행

        sql = 'insert into member(mem_name , tel , email , password) values("이길동","01032435432","zjhvhn@gmail.com","1235432"),("홍길동","01032223333","hasdfn@naver.com","4213432")'

        count =  cursor.execute(sql)
    #   commit
        db.commit()


    #     자원 정리
        cursor.close()
        db.close()
    #   결과 확인


        print(f'실행결과: {"성공"if count == 2 else "실패"}')

    except OperationalError as e:
        print(f'에러:{e}')