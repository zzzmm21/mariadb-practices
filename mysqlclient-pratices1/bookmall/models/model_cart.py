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

        sql = 'select count(*)as 수량, a.price as 가격 ,a.title as 제목 from book a , cart b ' \
              'where a.book_no = cart_no group by a.title;'
        cursor.execute(sql)

        results = cursor.fetchall()

        cursor.close()
        db.close()


        print('cart 리스트 가져오기')

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

        sql = 'insert into cart(member_mem_name, book_book_no, book_category_cate_no , cart_no) values("이길동","1","1","1"),("홍길동","2","2","2");'

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