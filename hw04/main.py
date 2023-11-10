from datetime import date
from service.Customer import Customer
from model.User import User

if __name__ == '__main__':
    user = User(1, "Guest", 2202123456789874)
    customer = Customer(user)
    customer.search_ticket(date(2023, 11, 11), 1)
    print(customer.search_ticket(date(2023, 11, 11), 1))
