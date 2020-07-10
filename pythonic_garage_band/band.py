class Band():
  """
  class band
  
  """
  band_list = []
  
  def __init__(self,name='NONE', memebers = ['jim , dwight']):
    self.name = name # band name 

  def __str__(self):
    return f"str band name, {self.name}"

  def __repr__(self):
    return f"repr band name: {self.name}"
  @classmethod
  def band_list(cls):
    print(cls)
    return cls.band_list
      
  class Muscian():
    artist_list = []
    def __int___ (self,name):
      self.name = name
      Muscian.artist_list.appen(self)
    def __str__(self):
      return f'str artist name: {self.name}'
    def __repr__(self):
      return f"artist repr, {self.name}"
    @classmethod 
    def to_list(cls):
      return cls.artist_list

  class Guitarist():
    def __int__(self, name='None'):
      self.name = name 
    def get_instrument(self):
      return 'guitar'
    def play_solos():
      return 'ripping the solo to shreds'
    
  class Bassist():
    def __init__(self, name='None'):
      self.name = name
    def get_instrument(self):
      return 'bass'
    def play_solo(self):
      return 'thumping away bass has never sounded so good'  
  
  class Drummer():
    def __init__(self, name= 'None'):
      self.name = name
    def __str__(self):
      return f'{self.name}'
    def get_instrument(self):
      return 'drums'
    def play_solos(self):
      return 'solo sounds like a machine gun its so fast'

if __name__ == "__main__":
  blink_182 = Band('blink-182')
  drums = blink_182.Drummer('travis barker')
  solo = drums.play_solos()
  print(blink_182)
  print(drums)
  print(solo)
