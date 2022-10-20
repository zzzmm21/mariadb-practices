from models import model_member
from models import model_category
from models import model_book
from models import model_cart
from models import model_orders
from models import model_orders_book
print('---회원리스트---')


def run_list():
    results = model_member.findall()

    for result in enumerate(results):
        print(result)

model_member.insert()
run_list()

print("---카테고리 리스트---")
def run_list():
    results = model_category.findall()

    for result in enumerate(results):
        print(result)
model_category.insert()
run_list()




print("---상품 리스트---")
def run_list():
    results = model_book.findall()

    for result in enumerate(results):
        print(result)
model_book.insert()
run_list()

print("---카트 리스트---")
def run_list():
    results = model_cart.findall()

    for result in enumerate(results):
        print(result)
model_cart.insert()
run_list()

print("---주문 리스트---")
def run_list():
    results = model_orders.findall()

    for result in enumerate(results):
        print(result)
model_orders.insert()
run_list()

print("---주문 도서 리스트---")
def run_list():
    results = model_orders_book.findall()

    for result in enumerate(results):
        print(result)
model_orders_book.insert()
run_list()


