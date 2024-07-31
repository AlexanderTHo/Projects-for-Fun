class Card:
    def __init__(self, attribute, name, cost, power, ability=None):
        self.attribute = attribute
        self.name = name
        self.cost = cost
        self.power = power
        self.ability = ability
        self.can_attack = False

    def use_ability(self, game, player):
        if self.ability:
            self.ability(game, player)

    def __str__(self):
        return f"{self.name} (Power: {self.power})"
    
#Abilities
def rush(game, player, card):
    print(f"[Rush] (This card can attack on the turn in which it is played.)")
    card.can_attack = True

def blocker(game, player):
    print(f"[Blocker] (After your opponent declares an attack, you may rest this card to make it the new target of the attack.)")
 
# Map ability 
ability_map = {
    "Rush": rush,
    "Blocker": blocker
}