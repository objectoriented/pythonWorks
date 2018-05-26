import io
import math
import string

maxNum=0

def printNumsToFile(maxNum, file):
    file = io.open(file, "w+", encoding="utf-8")
    for i in range(maxNum):
        if(i<1):
            i = 1
        else:
            file.write(str(i))
            file.write(" % ")
            file.write(str(2000))
            file.write(" = ")
            file.write(str(i%2000))
            file.write("\n")

printNumsToFile(5000, "nums.txt")