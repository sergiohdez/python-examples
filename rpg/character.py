class Character():

    # Create a character
    def __init__(self, char_name, char_description):
        """The constructor for the Character class"""
        self.name = char_name
        self.description = char_description
        self.conversation = None

    # Describe this character
    def describe(self):
        """The output string for Character object"""
        print( self.name + " is here!" )
        print( self.description )

    # Set what this character will say when talked to
    def set_conversation(self, conversation):
        """Set the conversation attribute to Character"""
        self.conversation = conversation

    # Talk to this character
    def talk(self):
        """The talk method for Character"""
        if self.conversation is not None:
            print("[" + self.name + " says]: " + self.conversation)
        else:
            print(self.name + " doesn't want to talk to you")

    # Fight with this character
    def fight(self, combat_item):
        """The fight method for Character"""
        print(self.name + " doesn't want to fight with you")
        return True

class Enemy(Character):
  quantity = 0
  
  def __init__(self, char_name, char_description):
    """The constructor for the Enemy class"""
    super().__init__(char_name, char_description)
    self.weakness = None
    Enemy.quantity += 1
  
  def set_weakness(self, item):
    """Set the weakness attribute to Enemy"""
    self.weakness = item
  
  def get_weakness(self):
    """Get the weakness attribute to Enemy"""
    return self.weakness
  
  def fight(self, combat_item):
    """The fight method for Enemy"""
    if combat_item == self.weakness:
      print("You fend " + self.name + " off with the " + combat_item)
      Enemy.quantity -= 1
      return True
    else:
      print(self.name + "crush you, punny adventurer")
      return False
  
  def steal(self):
    """The steal method for Enemy"""
    print("You steal some money from " + self.name)

class Friend(Character):
  
  def __init__(self, char_name, char_description):
    """The constructor for the Friend class"""
    super().__init__(char_name, char_description)
  
  def hugh(self):
    """The hugh method for Frined"""
    print(self.name + " hugs you back!")
