import model
import view

while model.play_game():
    used_letters = []
    available_letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O',
                         'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    wrong_answers = 0
    correct_word = model.get_word()
    hangword = model.get_hangword(correct_word)
    print('\n' * 100)
    user_letter = ''

    while '-' in hangword and wrong_answers < 6:
        view.draw_hangman(wrong_answers)
        view.show_hangword(hangword)
        view.available_letters(available_letters)
        view.used_letters(used_letters)

        user_letter = model.get_user_letter(available_letters)
        if model.letter_correct(user_letter, correct_word):
            hangword = model.replace_blank(user_letter, correct_word, hangword)
        else:
            view.incorrect_answer()
            wrong_answers = wrong_answers + 1

        available_letters.remove(user_letter)
        used_letters.extend(user_letter)

    view.draw_hangman(wrong_answers)

    if correct_word == hangword:
        view.user_won(correct_word)
    else:
        view.user_lost(correct_word)

    play = model.play_game()

print("Bye")
