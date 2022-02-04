
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