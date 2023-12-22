class Human:
  def __init__(self, name, age):
    self.name = name
    self.age = age
    
  def set_name(self, name):
    self.name = name
  def set_age(self, age):
    self.age = age
    
  def printinfo(self):
    print("名前:", self.name)
    print("年齢:", self.age)

human = Human("侍太郎", 18)

human.printinfo()