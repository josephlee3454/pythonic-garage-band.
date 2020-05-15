class Band():
  band_members_list = []
  def __init__(self,name,members):
    self.name = name 
    self.members = members
    self.band_members_list.append(self)
  print(band_members_list)
  def play_solos(self)
   pass
  class Muscian():
    def __int___ (self,name):
      self.name = name
    def __str__(self):
      return self.name
    def __repr__(self):
      return f"Musician, {self.name}"
  
  class guitarist():
    def __int__(self, name,model):
      super(),__init__(name)
      self.model = model 
    
    def __repr__(self):
        return f"Guitarist, {self.name}"

  # pass function for playing solos
#   def play_solos(self):
#     pass
#   @sataticmethod
#   def making_the_cut():
#     return "its time to make the band"
#   def __repr__(self)
#     retutn f'{self.name'}

# class guitar_player():
#   def __init__(self,name,instrument)
#     self.name = name
#     self. instrument = instrument
#   def get_instrument(self):
#     return "guitar"
#   def play_solo(self):
#     return "shred"