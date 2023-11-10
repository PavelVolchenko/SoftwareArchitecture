class TicketProvider:
    def __init__(self, date, route):
        self.date = date
        self.route = route

    @staticmethod
    def get_tickets():
        tickets = ['1234', '12342']
        return tickets

    def update_ticket(self, route):
        pass
