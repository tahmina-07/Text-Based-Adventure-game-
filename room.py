

class Room():
    
    number_of_rooms = 0
    def __init__(self, room_name):
        Room.number_of_rooms += 1
        self.name = room_name
        self.description = None
        self.linked_rooms = {}
        self.character = None
        self.item = None 
    
    def get_item(self):
        return self.item 
    
    def set_item(self, item_name):
        self.item = item_name

    def set_description(self, room_description):
        self.description = room_description

    def get_description(self):
        return self.description

    def set_name(self, room_name):
        self.name = room_name

    def get_name(self):
        return self.name

    def describe(self):
        print( self.description )

    def link_room(self, room_to_link, direction):
        self.linked_rooms[direction] = room_to_link
        # print( self.name + " linked rooms :" + repr(self.linked_rooms) )
    
    def get_details(self):
        print(self.name)
        print("----------------------")
        print(self.description)
        for d in self.linked_rooms:
            room = self.linked_rooms[d]
            print("The " + room.get_name() + " is " + d)
    
    def move(self, direction):
        if direction in self.linked_rooms:
            return self.linked_rooms[direction]
        else:
            print("You can`t go that way")
            return self 
    
    def set_character(self, character):
        self.character = character
    
    def get_character(self):
        return self.character
    
        