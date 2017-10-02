class Room():
  def __init__(self, room_name):
    """The constructor for the Room class"""
    self.name = room_name
    self.description = None
    self.linked_rooms = {}
    self.character = None
    self.item = None
  
  def set_description(self, room_description):
    """Set the description attribute for Room"""
    self.description = room_description
  
  def get_description(self):
    """Get the description attribute for Room"""
    return self.description
  
  def set_name(self, room_name):
    """Set the name attribute for Room"""
    self.name = room_name
  
  def get_name(self):
    """Get the name attribute for Room"""
    return self.name
  
  def set_character(self, new_character):
    """Set the character attribute for Room"""
    self.character = new_character
  
  def get_character(self):
    """Get the character attribute for Room"""
    return self.character
  
  def set_item(self, new_item):
    """Set the item attribute for Room"""
    self.item = new_item
  
  def get_item(self):
    """Get the item attribute for Room"""
    return self.item
  
  def describe(self):
    """The output string for Room"""
    print(self.description)
  
  def link_room(self, room_to_link, direction):
    """The link method for Room"""
    self.linked_rooms[direction] = room_to_link
    #print( self.name + " linked rooms :" + repr(self.linked_rooms) )

  def get_details(self):
    """The details for the Room"""
    print("The " + self.get_name())
    print("----------------------")
    print(self.get_description())
    for direction in self.linked_rooms:
      room = self.linked_rooms[direction]
      print("The " + room.get_name() + " is " + direction)
      
  def move(self, direction):
    """The move method for Room"""
    if direction in self.linked_rooms:
      return self.linked_rooms[direction]
    else:
      print("You can't go that way")
      return self
