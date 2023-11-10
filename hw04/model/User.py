class User:
    def __init__(self, id, name, card_number):
        self.id = id
        self.name = name
        self.card_number = card_number

    def get_id(self):
        return self.id

    def get_name(self):
        return self.name

    def get_card_number(self):
        return self.card_number

    def __str__(self):
        return f"ID: {self.id} Name: {self.name} Card: {self.card_number}"
