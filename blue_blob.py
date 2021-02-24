from blob import Blob
import color
import random

class BlueBlob(Blob):
  def __init__(self, blob_color, x_boundary, y_boundary):
    super().__init__(blob_color, x_boundary, y_boundary)
    self.color = color.BLUE
  
  def move_fast(self):
    self.x += random.randrange(-5,6)
    self.y += random.randrange(-5,6)