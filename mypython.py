import random
import string

files = ["iron.txt", "lithium.txt", "sodium.txt"] 

for file in files:
    randomString = ""
    i = 0
    while i < 10:
        randomString += random.choice(string.ascii_lowercase)
        i += 1

    f = open(file, "w+r")
    f.write(randomString)
    f.write("\n")
    f = open(file, "r")
    print(f.read(10))
    f.close()

from random import randint
randomInteger1 = randint(1, 42)
randomInteger2 = randint(1, 42)
print(randomInteger1)
print(randomInteger2)
print(randomInteger1 * randomInteger2)
