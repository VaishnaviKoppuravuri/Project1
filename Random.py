import random

n = random.randbytes(3)
print(n)
print(random.randrange(1, 8))
print(random.randint(100, 211))
mylist = ["Virat", "jadeja", "Dhoni", "Shami", "Rohit"]
mylist1 = {"Virat", "jadeja", "Dhoni", "Shami", "Rohit"}
print(random.choice(mylist))
random.shuffle(mylist)
print(mylist)
