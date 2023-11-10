class Ticket:
    def __init__(self, route, place, price, date):
        self.route = route
        self.place = place
        self.price = price
        self.date = date
        self.is_available = True

    def get_route(self):
        return self.route

    def get_valid(self):
        return self.is_available

    def get_date(self):
        return self.date

    def get_price(self):
        return self.price

    def set_is_available(self, status):
        self.is_available = status

    def __str__(self):
        return (f"route:{self.route}, date:{self.date}, price:{self.price}, "
                f"place: {self.place}, is available:{self.is_available}")
