class CashProvider:
    def __init__(self, customer):
        self.card_number = self.authorization(customer)
        self.is_authorized = None

    def buy(self):
        if self.is_authorized:
            return True
        return False

    def authorization(self, customer):
        self.is_authorized = True
        return customer.get_card_number()
