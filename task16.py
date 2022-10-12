'''
Task 16
Seth Maurice-Brant
'''

# NOTE: Not allowed to use split function.

def SentenceToWords(sentence):
    wordList = []
    nextWord = ""
    for character in sentence:
        if character == " ":
            wordList.append(nextWord)
            nextWord = ""
        else:
            nextWord += character
    return wordList

# Test

print(SentenceToWords("The quick brown fox jumped"))
