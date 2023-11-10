from abc import ABC, abstractmethod


class iCustomer(ABC):
    @abstractmethod
    def get_selected_tickets(self):
        pass

    @abstractmethod
    def set_selected_tickets(self, tickets):
        pass

    @abstractmethod
    def buy_ticket(self, ticket):
        pass

    @abstractmethod
    def search_ticket(self, date, route):
        pass
