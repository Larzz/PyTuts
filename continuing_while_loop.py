import random

playerhp = 400
enemyatk = 90
enemyatkh = 89

while playerhp > 0:
    dmg = random.randrange(enemyatk, enemyatkh)
    playerhp = playerhp - dmg

    if playerhp <= 30:
        playerhp = 30

    print('Enemy stricks for', dmg, 'points of damages', playerhp)

    if playerhp > 30:
        print('contnue')
        continue

    print("You have low health, you will be teleported to nearest inn.")
    break

