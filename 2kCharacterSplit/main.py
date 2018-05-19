import io
import string
import array
import math

userFileIn = input("File name? (do not include dot type): ")
textFromFile = io.open((str(userFileIn) + ".txt"), "r+", encoding="utf-8")
testText = textFromFile.read()
programFileOut = io.open("testwrite.txt", "a", encoding="utf-8")
arrayVar = []
varSplit = 2000
charCount = 0
charMaxCount = 0
numPosts = 0
textCon = 0


def TextIn(textString, charMaxCount=0, charCount=0, textCon=0):

    for i in textString:
        # discord counts white spaces
        charMaxCount += 1
        arrayVar.append(i)
    notComplete = True
    programFileOut.write("\n")
    while(notComplete):
        if(charCount != charMaxCount):
            print(str(arrayVar[charCount]), end="")
            programFileOut.write((str(arrayVar[charCount])))
            charCount += 1
        elif((charCount == charMaxCount) and (textCon < 1)):
            programFileOut.write("\n ------------NEW POST------------")
            textCon += 1

        else:
            numPosts = (math.ceil((len(textString) / 2000)))
            notComplete = False

    print("\n")
    print("Number of characters being processed: " + str(charMaxCount))
    print("Number of posts to send entire message: " + str(numPosts))

TextIn(testText)
