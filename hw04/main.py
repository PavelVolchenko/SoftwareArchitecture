from service import Customer
from model import User

if __name__ == '__main__':
    user = User(1, "Guest", 2202123456789874)
    customer = Customer(user)