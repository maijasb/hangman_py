def show_hangword(hangword):
    print(f"Hangword is {' '.join(hangword)}")


def incorrect_answer():
    print("Letter is not in word")
    

def available_letters(letters):
    print(f"Letters available: {' '.join(letters)}")


def used_letters(letters):
    print(f"Used letters: {' '.join(letters)}")

    
def user_won(correct_word):
    print(f"You're very smart and you guessed the word {' '.join(correct_word)}")


def user_lost(correct_word):
    print(f"Correct word was {' '.join(correct_word)}. Better luck next time")

class bcolors:
    FAIL = '\033[91m'
    ENDC = '\033[0m'


def draw_hangman(wrong_answers):
    if wrong_answers == 0:
        print(
            r'''
              -------
             |      |
             | 
             | 
             |     
             |     
             |
            '''
        )

    elif wrong_answers == 1:
        print(
            r'''
              -------
             |      |
             |      O
             | 
             | 
             | 
             |
            '''
        )

    elif wrong_answers == 2:
        print(
            r'''
              -------
             |      |
             |      O
             |      |
             |      |
             | 
             |
            '''
        )

    elif wrong_answers == 3:
        print(
            r'''
              -------
             |      |
             |      O
             |      |\
             |      |
             | 
             |
            '''
        )

    elif wrong_answers == 4:
        print(
            r'''
              -------
             |      |
             |      O
             |     /|\
             |      |
             | 
             |
            '''
        )

    elif wrong_answers == 5:
        print(
            r'''
              -------
             |      |
             |      O
             |     /|\
             |      |
             |     / 
             |
            '''
        )

    elif wrong_answers == 6:
        print(
            r'''
              -------
             |      |
             |      O
             |     /|\
             |      |
             |     / \
             |
            '''
        )
        print(f"{bcolors.FAIL}You dead!{bcolors.ENDC}")
