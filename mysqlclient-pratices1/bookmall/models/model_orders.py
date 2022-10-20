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

        sql = 'select c.order_no, a.mem_name ,a.email, sum(price), c.adress as 주소 from member a, book b , orders c , cart d where b.book_no = d.book_book_no and d.member_mem_name = a.mem_name and a.mem_name = c.member_mem_name;'
        cursor.execute(sql)

        results = cursor.fetchall()

        cursor.close()
        db.close()


        print(' 주문 리스트 가져오기')

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

        sql = 'insert into orders(order_no, adress, member_mem_name) values("1","서울시","이길동")'

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