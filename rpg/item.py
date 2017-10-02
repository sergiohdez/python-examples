#from room import Room

class Item():
  def __init__(self, item_name, item_description):
    """The constructor for the Item class"""
    self.name = item_name
    self.description = item_description
  
  def set_name(self, item_name):
    """Set the name attribute for Item"""
    self.name = item_name
  
  def get_name(self):
    """Get the name attribute for Item"""
    return self.name
  
  def set_description(self, item_description):
    """Set the description attribute for Item"""
    self.description = item_description
  
  def get_description(self):
    """Get the description attribute for Item"""
    return self.description
  
  def describe(self):
    """The output string for Item"""
    print("The [" + self.name + "] is here - " + self.description)
