import io
import string
import array
import math

userFileIn = input("File name? (do not include extention): ")
textFromFile = io.open((str(userFileIn) + ".txt"), "r+", encoding="utf-8")
testText = textFromFile.read()
programFileOut = io.open("testwrite.txt", "a", encoding="utf-8")
arrayVar = []
varSplit = 2000
charCount = 0
charMaxCount = 0
numPosts = 0
textCon = 0
letter = 0


def TextIn(textString, charMaxCount=0, charCount=0, numPosts=0, newPostCounter=0, letter=0, post=True):
    for i in textString:
        # discord counts white spaces
        charMaxCount += 1
        arrayVar.append(i)
    notComplete = True
    while(notComplete):
        if( letter != charMaxCount):
            #print(str(arrayVar[charCount]), end="")
            while(post):
                if ((charCount != varSplit)) and ((charCount + newPostCounter) != charMaxCount):
                    programFileOut.write((str(arrayVar[letter])))
                    charCount += 1
                    letter+=1
                else:
                    if (newPostCounter == charMaxCount):
                        charCount = newPostCounter
                        post = False
                        break
                    programFileOut.write("\n ------------NEW POST------------ \n")
                    newPostCounter += charCount
                    charCount = 0
        else:
            numPosts = (math.ceil((len(textString) / 2000)))
            notComplete = False
    print("\n")
    print("Number of characters being processed: " + str(charMaxCount))
    print("Number of posts to send entire message: " + str(numPosts))

TextIn(testText)