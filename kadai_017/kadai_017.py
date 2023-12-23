class Human:
  def __init__(self, name, age):
    self.name = name
    self.age = age
  
  def check_adult(self):
    if self.age >= 20:
      print(f"{self.name}さんは{self.age}才なので大人です。")
    else:
      print(f"{self.name}さんは{self.age}才なので大人ではありません。")

data = [
        ["山田", 10],
        ["田中", 15],
        ["加藤", 25]
        ]

human_list = []
for d in data:
  human_list.append((d[0], d[1]))
  
i = 0
for h in human_list:
  Human(h[0], h[1]).check_adult()