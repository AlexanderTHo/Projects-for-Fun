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