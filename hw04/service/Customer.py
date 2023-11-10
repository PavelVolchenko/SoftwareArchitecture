from hw04.interface.iCustomer import iCustomer


class Customer(iCustomer):
    def __init__(self, user):
        self.customer = user

    def get_selected_tickets(self):
        pass

    def set_selected_tickets(self, tickets):
        pass

    def buy_ticket(self, ticket):
        pass

    def search_ticket(self, date, route):
        pass

