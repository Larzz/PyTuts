import random

'''
    Program: Check Class Defense Points
    Author: Larry
    Copyright: 2020
'''

class Enemy:
    hp = 20

    def __init__(self, attackpoints, defensepoints):  # instance variable
        self.attackpoints = attackpoints
        self.defensepoints = defensepoints

    # class function
    def getAttach(self):
        print(self.attackpoints)

    # class function
    def getDefense(self):
        print(self.defensepoints)

    def getHp(self):
        print(self.hp)


enemy = Enemy(attackpoints=12, defensepoints=2)  # calling
enemy.getAttach()

enemy2 = Enemy(defensepoints=23, attackpoints=2)  # calling
enemy2.getDefense()

enemy2 = Enemy(defensepoints=23, attackpoints=2)  # calling
enemy2.getHp()
