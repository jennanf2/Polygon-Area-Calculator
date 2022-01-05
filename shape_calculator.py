class Rectangle:
  def __init__(self, w, h):
    self.width = w
    self.height = h

  def __str__(self):
    return "Rectangle(width=" + str(self.width) + ", height=" + str(self.height) + ")"

  def set_width(self, w):
    self.width = w
  
  def set_height(self, h):
    self.height = h
  
  def get_area(self):
    return self.width * self.height

  def get_perimeter(self):
    return 2 * self.width + 2 * self.height

  def get_diagonal(self):
    return (self.width ** 2 + self.height ** 2) ** .5

  def get_picture(self):
    if (self.width > 50 or self.height > 50):
      return "Too big for picture."
    picture = ""
    for h in range(self.height):
      for w in range(self.width):
        picture = picture + "*"
      picture = picture + "\n"
    return picture

  def get_amount_inside(self, shape):
    if (shape.width > self.width or shape.height > self.height):
      return 0
    widthMax = 0
    original = self.width
    while (original >= shape.width):
      original-=shape.width
      widthMax+=1
    heightMax = 0
    originalH = self.height
    while (originalH >= shape.height):
      originalH-=shape.height
      heightMax+=1
    return widthMax*heightMax

class Square(Rectangle):
  def __init__(self, s):
    super().__init__(s, s)

  def __str__(self):
    return "Square(side=" + str(self.width) + ")"

  def set_side(self, s):
    self.width = s
    self.height = s

  def set_width(self, s):
    self.width = s
    self.height = s

  def set_height(self, s):
    self.width = s
    self.height = s

  
