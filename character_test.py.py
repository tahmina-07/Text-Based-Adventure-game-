from character import Enemy

dave = Enemy("Dave", "A smelly zombie!")
dave.describe()
dave.set_conversation("I am Dave a smelly zombie!")
dave.talk()
dave.set_weakness("Cheese")
print("What will you fight with?")
fight_with = input()
dave.fight(fight_with)

