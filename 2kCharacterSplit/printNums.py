import io
import math
import string

maxNum=0

def printNumsToFile(maxNum, file):
    file = io.open(file, "w+", encoding="utf-8")
    for i in range(maxNum):
        file.write(str(i+1))
        file.write("\n")