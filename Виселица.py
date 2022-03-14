from random import choice
word_list = ["Человек", "Солнце", "Собака", "Дорога", "Машина", "Карусель", "Дом", "Семья", "Школа"]

def get_word():
    word = choice(word_list)
    return word.upper()

def display_hangman(tries):
    stages = [# финальное состояние: голова, торс, обе руки, обе ноги
                '''
                   --------
                   |      |
                   |      O
                   |    --|--
                   |      |
                   |     / \
                   -
                ''',
                # голова, торс, обе руки, одна нога
                '''
                   --------
                   |      |
                   |      O
                   |    --|--
                   |      |
                   |     / 
                   -
                ''',
                # голова, торс, обе руки
                '''
                   --------
                   |      |
                   |      O
                   |    --|--
                   |      |
                   |      
                   -
                ''',
                # голова, торс и одна рука
                '''
                   --------
                   |      |
                   |      O
                   |    --|
                   |      |
                   |     
                   -
                ''',
                # голова и торс
                '''
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |     
                   -
                ''',
                # голова
                '''
                   --------
                   |      |
                   |      O
                   |    
                   |      
                   |     
                   -
                ''',
                # начальное состояние
                '''
                   --------
                   |      |
                   |      
                   |    
                   |      
                   |     
                   -
                '''
    ]
    return stages[tries]

def guess_input(guessed_letter):
    guess = input('Введите букву - ')
    while True:
        if guess.isalpha() != True:
            guess = input('Пожалуйста, введите букву или слово целиком - ')
        elif guess in guessed_letter == True:
            guess = input('Вы уже вводили эту букву, попробуйте ввести другую - ')
        else:
            return guess.upper()

def play():
    while True:
        word = get_word()
        word_completion = ['_']*len(word)
        guessed = False
        guessed_letters = []
        guessed_words = []
        tries = 6
        print('Давайте играть в Виселицу!', display_hangman(tries), word_completion, sep="\n")
        while guessed == False:
            guess = guess_input(guessed_letters)
            if guess == word:
                word_completion = word
                print('Великолепно, вы угадали слово!', display_hangman(tries), sep='\n')
                print(*word_completion)
                guessed_words += word
                guessed = True
            elif guess in list(word):
                count = 0
                for i in range(len(word)):
                    if word[i] == guess:
                        word_completion[i] = guess
                        count += 1
                if word_completion == list(word):
                    print('Великолепно, вы угадали слово!', display_hangman(tries), sep='\n')
                    print(*word_completion)
                    guessed_words += word
                    guessed = True
                else:
                    print(f'Отлично, вы угадали {count} букв!', display_hangman(tries), sep='\n')
                    print(*word_completion)
            else:
                tries -= 1
                print('Упс, неправильно! Попробуйте ещё раз', display_hangman(tries), sep='\n')
                print(*word_completion)
        cont = input('Хотите сыграть ещё раз? (да/нет) - ')
        if cont in ('нет', 'ytn', 'no'):
            break

play()



