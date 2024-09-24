import random

print("Welcome to The game of Word Guess")
username = input("Name: ")
word_choice=['bright','champs','coding','python','student','online']
secret_word=word_choice[random.randint(0,len(word_choice)-1)]
guessed_letters=""
lives=10
finished_word=""
def lines():
    global finished_word
    for i in secret_word:
        if i in guessed_letters:
            print(i,end=" ")
            finished_word+=i
        else:
            print("_",end=" ")
lines()
while True:
    user_letter=input("\nInput  a letter: ")
    guessed_letters+=user_letter
    finished_word=""
    if user_letter not in secret_word:
        for i in user_letter:
            if i not in secret_word:
                if lives > 0:
                    lives -= 1
                else:
                    lives=0
        print("\nWrong Guess")
        print("Lives: ", lives)
    if lives==0:
        print("You ran out of lives")
        break
    lines()
    if secret_word == finished_word:
        print("\nCongratulations, ",username," You win the game")
        print("The word is",secret_word)
        break