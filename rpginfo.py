class RPGInfo():
    author = "Tahmina Sahar"
    def __init__(self, game_title):
        self.title = game_title
    
    def welcome(self):
        print("Welcome to " + self.title)
    
    @staticmethod 
    def info():
        print("Made using the OOP RPG game creator (c) Tahmina Sahar")
    
    @classmethod 
    def credits(cls):
        print("Thank you for playing")
        print("Created by " + cls.author)
    
    