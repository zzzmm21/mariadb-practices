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

        sql = 'select title as 제목 , price  as 가격 from book'
        cursor.execute(sql)

        results = cursor.fetchall()

        cursor.close()
        db.close()


        print('상품 리스트 가져오기')

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

        sql = 'insert into book(book_no,title,price,category_cate_no) values("1","자바의정석","25000","1"),("2","파이썬의정석","35000","2"),("3","수학의정석","15000","3")'
        count =  cursor.execute(sql)
    #   commit
        db.commit()


    #     자원 정리
        cursor.close()
        db.close()
    #   결과 확인


        print(f'실행결과: {"성공"if count == 3 else "실패"}')

    except OperationalError as e:
        print(f'에러:{e}')