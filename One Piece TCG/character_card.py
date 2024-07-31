from base_card import Card

class CharacterCard(Card):
    def __init__(self, attribute, name, cost, power, counter, ability=None):
        super().__init__(attribute, name, cost, power, ability)
        self.counter = cost
        self.counter = counter

    def __str__(self):
        return f"{self.name} (Cost: {self.cost}, Power: {self.power}, Counter: {self.counter})"