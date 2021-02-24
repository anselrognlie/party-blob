from blob import Blob
import color
import random

class BlueBlob(Blob):
  def __init__(self, x_boundary, y_boundary):
    super().__init__(color.BLUE, x_boundary, y_boundary)
  
  def move_fast(self):
    self.x += random.randrange(-5,6)
    self.y += random.randrange(-5,6)

  def __add__(self, other_blob):
      if other_blob.color == color.RED:
          self.size -= other_blob.size
          other_blob.size -= self.size
          
      elif other_blob.color == color.GREEN:
          self.size += other_blob.size
          other_blob.size = 0
          
      elif other_blob.color == color.BLUE:
          # for now, nothing. Maybe later it does something more. 
          pass
      else:
          raise Exception('Tried to combine one or multiple blobs of unsupported colors!')
