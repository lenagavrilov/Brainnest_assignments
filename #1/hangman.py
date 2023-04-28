'''
The hangman game is a word guessing game where the player is given a word and has to guess the letters that make up the word.
The player is given a certain number of tries (no more than 6 wrong guesses are allowed) to guess the correct letters before the game is over.
'''

# Output
'''
You have 6 tries left.                                                                                                                                           
Used letters:                                                                                                                                                    
Word: _ _ _ _                                                                                                                                                    
Guess a letter: a 

You have 6 tries left.                                                                                                                                           
Used letters: a                                                                                                                                                  
Word: _ a _ a                                                                                                                                                    
Guess a letter: j    

You have 6 tries left.                                                                                                                                           
Used letters: j a                                                                                                                                                
Word: j a _ a                                                                                                                                                    
Guess a letter: v                                                                                                                                                
You guessed the word java !
'''

def hangman(word_to_guess):
    global used_letters
    global word_result

    #print(word_to_guess)
    word_result = ''
    used_letters = []

    for letter in word_to_guess:
        word_result = word_result + '_'

    printResultWord()

    total_wrong_guesses = 6
    wrong_guess_num = 0

    while wrong_guess_num < total_wrong_guesses:
        print() #Add blank line to easily distinguish between tries

        letter_found = False

        print('You have ' + str(total_wrong_guesses-wrong_guess_num) + ' wrong guesses left.')
        print('Used letters: ', ' '.join(used_letters))

        guess = input("Guess the letter (or type 'exit' to exit the program): ")

        if guess == 'exit':
            exit(0)

        if checkInput(guess):
            used_letters.append(guess)
        else:
            printResultWord()
            continue

        for i, letter in enumerate(word_to_guess):
            if guess.lower() == letter.lower():
                temp = list(word_result)
                temp[i] = guess
                word_result = ''.join(temp)
                letter_found = True

        if letter_found:
            printResultWord()
        else:
            print('No Match')
            printResultWord()
            wrong_guess_num +=1

        if not '_' in word_result:
            print('You WON')
            exit(0)

    print('You LOSE!')
    print('The correct word is: ' + word_to_guess)
    exit(0)


def checkInput(guess):
    if not guess.isalpha() or len(guess) != 1:  # Guess is one letter only
        print("You have to enter exactly one letter. Try again")
        return False

    if guess in used_letters:  # To follow the letters which were already typed in
        print('This letter is used already')
        return False

    return True


def printResultWord():
    print('Word: ' + word_result )


if __name__ == "__main__":
    hangman('python')

