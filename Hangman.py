import random

def getword():
    file = open("wordlist.txt")
    fin = file.readlines()
    n = random.randint(0, 58109)
    word = fin[n].strip()
    return word
def getInstances(word, guess):
    ocurs = list()
    for i, char in enumerate(word):
        if guess == char:
            ocurs.append(i)
    return ocurs
def updateString(string, index, guess, length):
    tmp = ""
    for i in range(length-1):
        if i == index:
            tmp += guess
        else:
            tmp += string[i]
    return tmp
def main():
    win = False
    lost = False
    word = getword()
    string = '_'*len(word)
    lives = 5
    while(win == False and lost == False):
        print(string)
        guess = input("Input single character or guess the entire word: ") 
        if guess == word or string == word:
            print(f"Correct! The word was {word}, you win!")
            win = True
        if guess in word and len(guess) == 1:
            ocurs = getInstances(word, guess)
            for i in range(len(ocurs)):
                string = updateString(string, ocurs[i], guess, len(word)) 
        else:
            lives -=1
        if lives == 0:
            print(f"YOU LOSE! The answer was {word}")
            lost = True
if __name__ == "__main__":
    main()