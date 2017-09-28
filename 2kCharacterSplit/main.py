##import io
import string
import array

testText = """“I’ll have to find a potential apprentice to do something about that,” Medivh mused, stretching Khadgar’s palm between his hands and running his thumbs along the heel of his hand. “Someone impudent, impetuous, confident, intelligent, headstrong, overachieving, and stubborn to a fault, perhaps.”
Khadgar chuckled. “Sounds familiar. I’m sure you’ll find exactly who you need.”
Medivh kissed Khadgar’s palm. “No doubt,” he said softly. “And once the library is organized again, I can take that apprentice to my bed, and spoil him.”
Khadgar blushed. “I –“
Medivh shushed him with a finger against his lips, kissing the inside of Khadgar’s wrist, then the inside of his elbow. Khadgar closed his eyes, shivering slightly. “Enough talking,” Medivh murmured, leaning to touch his lips to Khadgar’s. “There are more important things that should be coming out of your mouth than work talk.” He kissed down the younger mage’s throat, chuckling as Khadgar’s head lifted and offered more space. His hands traced nonsense along shoulders and chest, followed by soft kisses.
Medivh’s lips and fingers found sensitive spots and exploited them fully, a brush of fingertip here, a light scrape of nail there, a nip following the ghosting of lips. He worked his way down Khadgar’s body, smiling wickedly at the way his apprentice’s hands curled into the fabric beneath them, twined in the comforter white knuckled and trembling. “Let me hear you,” he murmured against the skin of his hip. “That Mageroyal must be working by now, hm?”
Khadgar sighed sharply, the barest hint of a moan slipping past. “Medivh,” he murmured. “I…” Medivh chuckled, biting at the top of one thigh and drawing a yelp.
“This isn’t part of the Game. You are allowed to retaliate, remember…” Medivh reminded him.
“When you turn my mind to mush like this? You want me to do more than ju—Ah!” Khadgar yelped again as the other thigh was nipped, then soothed with a swipe of Medivh’s tongue. The Mageroyal was indeed doing its job; he was half-hard already.
“Than just feel? Fair.” Medivh leaned up, running his tongue along Khadgar’s tip, teasing his former apprentice into full hardness – and drawing a darker moan, and a soft curse in the process. “Light, the things you do to me,” he murmured, nipping at the skin of Khadgar’s stomach. “You make me want to throw my intentions out the window…”
“Why don’t you?” Khadgar shot back, breathless.
“Don’t tempt me,” Medivh hissed, biting down on one nipple sharply and shuddering at Khadgar’s cry. “Oh, don’t tempt me.” He leaned to bite the other, then looked up to admire his work. Khadgar’s eyes were as dark as twilight, already glowing faintly. The little marks against his skin where Medivh had bitten were reddening beautifully. His chest rose and fell rapidly, though evenly. His cock twitched with impatience, his essence beading at the tip.
 """
stringVar = ""
arrayVar = []
varSplit = 2000
charCount = 0
charMaxCount = 0

def TextIn(textString, charMaxCount=0, charCount=0):
    #print(str(textString))
    #charCount = len(testText)
    print(varSplit)
    while charCount != len(textString):
        charMaxCount = 0

        for i in str(textString):
            # discord counts white spaces
            if charMaxCount <= len(textString):
                charCount += 1
                charMaxCount += 1
                arrayVar.append(i)
        for i in range(varSplit):
            print(str(arrayVar[i]), end="")




    print("\n")
    #print(str(arrayVar))
    print(charMaxCount)
    if varSplit == textString:
        print("true")
    else:
        print("false")

TextIn(testText)