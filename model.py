def play_game():
    play = input("Let's play hangman? (Y/N) ")
    while play not in ['Y', 'y', 'N', 'n']:
        play = input("I don't understand, choose Y or N")
    if play == 'Y' or play == 'y':
        play = True
    else:
        play = False
    return play


def get_word():
    word = input("What will be the hangword to guess? ").upper()
    while not word.isalpha():
        print("Please choose a valid word")
        word = input("What will be the hangword to guess? ")
    return list(word.upper())


def get_hangword(word):
    return list("-" * len(word))


def get_user_letter(available_letters):
    user_letter = input("Choose a letter ").upper()
    while not (user_letter.isalpha() and user_letter in available_letters):
        print("Choose valid letter")
        user_letter = input("Choose a letter ").upper()
    return user_letter.upper()


def letter_correct(user_letter, word):
    return user_letter in word


def replace_blank(user_letter, correct_word, hangword):
    index = 0
    for _ in correct_word:
        if correct_word[index] == user_letter:
            hangword[index] = user_letter
        index += 1
    return hangword
