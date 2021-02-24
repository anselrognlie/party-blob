from blob import Blob
import color

class GreenBlob(Blob):
  def __init__(self, x_boundary, y_boundary):
    super().__init__(color.GREEN, x_boundary, y_boundary)
  