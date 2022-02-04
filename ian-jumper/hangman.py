#loop with max turn count
#input guess
#check guess
#if wrong increase count
#if correct print correct letter guess
#if all correct break loop
#if guess number exceeded break loop with game over


#secret word start
guessWord = "mcmuffin"
lettersGuessed = ""

#The number of turns before game over
gameOverCount = 6

while gameOverCount > 0:

    
    #get the guess letter
    guess = input("Enter a letter: ")

    if guess in guessWord:
        #player gets letter correct
        print(f"Correct guess! There is one or more {guess} in the secret word")
    else:
        gameOverCount -= 1 
        print(f"Incorrect, There are no {guess} in the secret word. {gameOverCount} turn(s) left.")

    lettersGuessed = lettersGuessed + guess
    wrongLetterCount = 0

    for letter in guessWord:
        if letter in lettersGuessed:
            print(f"{letter}", end="")
        else:
            print("_", end="")
            wrongLetterCount += 1

    if wrongLetterCount == 0:
        print(f" Congratulations! The secret word was: {guessWord}. You win!")
        break

    
else:
    print("Game Over, please try again.")


import random
from words import word_list

class game:


  def get_word():
    word = random.choice(word_list)
    return word

def play(word):
    full_word = "_" * len(word)
    guessed = 0
    guessed_words = []
    guessed_letters = []
    tries = 8
    print('The Code Worked')



def display_parachute(tries):
    attempts = ['''
               ____
              /____\
              \    /
               \  /
                 O
                \|/
                 |
                / \ 
            ,

              /____\
              \    /
               \  /
                 O
                \|/
                 |
                / \ 
            ,

               ____\
              \    /
               \  /
                 O
                \|/
                 |
                / \ 
            ,

                   \
              \    /
               \  /
                 O
                \|/
                 |
                / \ 
            ,

              \    /
               \  /
                 O
                \|/
                 |
                / \ 
            ,

                   /
               \  /
                 O
                \|/
                 |
                / \ 
            ,
            
               \  /
                 O
                \|/
                 |
                / \ 
            ,

                  /
                 O
                \|/
                 |
                / \ 
            ,

                 O
                \|/
                 |
                / \ 
            '''
            ]

    return attempts(tries)
                  

def main():
      word = get_word()
      play(word)
      again = input('Would you like to play again (y/n)')
      while again == "y":
          word = get_word()
          play(word)
      else:
        print('Thanks for playing')








