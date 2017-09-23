import random
import io
random.seed()

def rNum(a=None, b=None):
    if a == "":
        a = input("First number ")
    elif b == "":
        b = input("Second number ")

    randPrint = random.randrange(int(a), int(b))

    print(randPrint)
rNum(5, 9)

