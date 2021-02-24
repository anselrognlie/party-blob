from blob import Blob
import color
import random

class RedBlob(Blob):
  def __init__(self, x_boundary, y_boundary):
    super().__init__(color.RED, x_boundary, y_boundary)
  
  def move_fast(self):
    self.x += random.randrange(-5,6)
    self.y += random.randrange(-5,6)
