from base_card import Card

class LeaderCard(Card):
    def __init__(self, attribute, life, name, cost, power, ability=None):
        super().__init__(attribute, name, cost, power, ability)
        self.life = life

    def __str__(self):
        return f"{self.name} (Power: {self.power}, Life: {self.life})"