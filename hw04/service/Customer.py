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
        tickets = {
            1: ["#1234-1234", "#4321-4321"],
            2: ["#0987-0987", "#7890-7890"],
            3: ["#5555-5555", "#6666-6666"],
        }
        return tickets.get(route)
