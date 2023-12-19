import random

ver = random.randint(0, 100)

print(ver)

if ver % 3 == 0 and ver % 5 == 0:
  print("FizzBuzz")

elif ver % 3 == 0:
  print("Fizz")

elif ver % 5 == 0:
  print("Buzz")

else: print(ver)