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

        sql = 'select a.book_no,a.title , b.count as 수량 from book a , orders_book b where a.book_no = b.book_book_no'
        cursor.execute(sql)

        results = cursor.fetchall()

        cursor.close()
        db.close()


        print(' 주문 도서 리스트 가져오기')

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

        sql = 'insert into orders_book(book_book_no, book_category_cate_no, orders_order_no, orders_member_mem_name, count) values("1","1","1","홍길동","1"),("2","2","2","김길동","1")'
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