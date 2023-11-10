from ..interface import iCustomer
from ..model import User


class Customer(iCustomer):
    def __init__(self):
        self.customer = User

    def get_selected_tickets(self):
        pass

    def set_selected_tickets(self, tickets):
        pass

    def buy_ticket(self, ticket):
        pass

    def search_ticket(self, date, route):
        pass
