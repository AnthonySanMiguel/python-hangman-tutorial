# The Hangman program randomly selects a secret word from a list of secret words.
# The random module will provide this ability, so this line imports it.
import random

# Normal strings are one line and have one quote character at the start and end.
# However, if you use three quotes at the start and end, then the string can go across several lines:
# This a 'multi-line' string: the newline characters are included as part of the string.
# You don’t have to use the \n escape character, or escape quotes as long as you don’t use three of them together.

# In Python, naming convention for constant variables is all capitals.

HANGMANPICS = ['''

   +---+
   |   |
       |
       |
       |
       |
 =========''', '''

   +---+
    |   |
    O   |
        |
        |
        |
  =========''', '''

    +---+
    |   |
    O   |
    |   |
        |
        |
  =========''', '''

    +---+
    |   |
    O   |
   /|   |
        |
        |
  =========''', '''

    +---+
    |   |
    O   |
   /|\  |
        |
        |
  =========''', '''
  
    +---+
    |   |
    O   |
   /|\  |
   /    |
        |
  =========''', '''

    +---+
    |   |
    O   |
   /|\  |
   / \  |
        |
  =========''']

words = 'ant baboon badger bat bear beaver camel cat clam cobra cougar coyote crow deer dog donkey duck eagle ferret fox frog goat goose hawk lion lizard llama mole monkey moose mouse mule newt otter owl panda parrot pigeon python rabbit ram rat raven rhino salmon seal shark sheep skunk sloth snake spider stork swan tiger toad trout turkey turtle weasel whale wolf wombat zebra'.split()

# Will take a list of strings passed to it, and return one string from it
def getRandomWord(wordList):
    # This function returns a random string from the passed list of strings.
    wordIndex = random.randint(0, len(wordList) - 1)
    # Will return the element in wordList at the integer index stored in wordIndex.
    return wordList[wordIndex]

# 'displayBoard' function takes the following 4 parameters:
#   HANGMANPICS - A list of multi-line strings that will display the board as ASCII art (global variable).
#   missedLetters - A string of the letters the player has guessed that are not in the secret word.
#   correctLetters - A string of the letters the player has guessed that are in the secret word.
#   secretWord – A string of the secret word that the player is trying to guess.
def displayBoard(HANGMANPICS, missedLetters, correctLetters, secretWord):
    # The first print() function call will display the board.
    #   HANGMANPICS will be a list of strings for each possible board.
    #   HANGMANPICS[0] shows an empty gallows,
    #   HANGMANPICS[1] shows the head (when the player misses one letter),
    #   HANGMANPICS[2] shows a head and body (when the player misses two letters),
    #   and so on until HANGMANPICS[6] which shows the full hangman.

    # The number of letters in missedLetters will reflect how many incorrect guesses the player has made.
    # Call len(missedLetters) to find out this number. So, if missedLetters is 'aetr' then len('aetr') will return 4.
    # Printing HANGMANPICS[4] will display the appropriate hangman board for 4 misses.
    # This is what HANGMANPICS[len(missedLetters)] on the next line evaluates to.
    print(HANGMANPICS[len(missedLetters)])
    print()

    # Prints the string 'Missed letters:' with a space character at the end instead of a newline
    print('Missed letters:', end=' ')
    # Will iterate over each character in the missedLetters string and print them on the screen. Remember that the end=' ' will replace the newline character that is printed after the string with a single space character.
    for letter in missedLetters:
        print(letter, end=' ')
    print()

    # Creates the blanks variable full of _ underscores using string replication. Remember that the * operator can also be used on a string and an integer, so the expression '_' * 5 evaluates to '_____'. This will make sure that blanks has the same number of underscores as secretWord has letters.
    blanks = '_' * len(secretWord)

    # A for loop goes through each letter in secretWord and replaces the underscore with the actual letter if it exists in correctLetters.
    for i in range(len(secretWord)):  # replace blanks with correctly guessed letters
        if secretWord[i] in correctLetters:
            blanks = blanks[:i] + secretWord[i] + blanks[i + 1:]

    # Print the new value of blanks with spaces between each letter.
    for letter in blanks:  # show the secret word with spaces in between each letter
        print(letter, end=' ')
    print()

# 'getGuess' function returns the letter the player inputs as a string, and validates that the data input is in fact a letter
def getGuess(alreadyGuessed):
    # Returns the letter the player entered. This function makes sure the player entered a single letter, and not something else.
    # While loop that will continue to prompt player to enter a letter until:
    # 1) A single letter is entered
    # 2) A single letter is entered that has not already been previously entered (guessed)
    while True:
        print('Guess a letter.')
        guess = input()
        # If player enters an uppercase letter, it will be turned into and overwritten as a lowercase one
        guess = guess.lower()
        # If user enters more characters than one...
        if len(guess) != 1:
            print('Please enter a single letter.')
        # Else If, user enters a letter they already used before
        elif guess in alreadyGuessed:
            print('You have already guessed that letter. Choose again.')
        # Else If, user enters any other character other than a lowercase alpha character (since capital letters will be converted to lowercase as mentioned above)
        elif guess not in 'abcdefghijklmnopqrstuvwxyz':
            print('Please enter a LETTER.')
        else:
            return guess

def playAgain():
    # This function returns True if the player wants to play again, otherwise it returns False.
    print('Do you want to play again? (yes or no)')
    # Converts user input to lowercase, and checks if entered character or word begins with lowercase 'y'
    return input().lower().startswith('y')

print('H A N G M A N')  # First 'print()' call when game is executed
missedLetters = ''  # Assigns blank strings for both 'missedLetters' and 'correctLetters' since user has not made any guesses at start of game
correctLetters = ''
secretWord = getRandomWord(words)  # Will retrieve a random word from the list of strings
gameIsDone = False

# The while loop’s condition is always True, which means it will loop forever until a break statement is encountered.
while True:
    # Calls the displayBoard() function, passing it the list of hangman ASCII art pictures
    # and the three variables set above (missedLetters, correctLetters, secretWord).
    # Based on how many letters the player has correctly guessed and missed, this function displays the appropriate hangman board to the player.
    displayBoard(HANGMANPICS, missedLetters, correctLetters, secretWord)

    # Let the player type in a letter.
    # The getGuess() function needs all the letters in missedLetters and correctLetters combined, so line 116 concatenates the strings in these variables and passes the result as the argument.
    # This argument is needed by getGuess() because the function has to check if the player types in a letter that they have already guessed.
    guess = getGuess(missedLetters + correctLetters)

    # If the guess string exists in secretWord, then concatenate guess to the end of the correctLetters string.
    # This string will be the new value of correctLetters.
    if guess in secretWord:
        correctLetters = correctLetters + guess

        # Check if the player has won...
        # A. - 'foundAllLetters' starts off assuming all letters of secret word have been found (or guessed)
        foundAllLetters = True
        # Iterate over each letter in secretWord and see if it exists in correctLetters
        # If every letter in secretWord exists in correctLetters, the player wins
        for i in range(len(secretWord)):
            # B. - However, if a letter is found in the secretWord that is not in correctLetters (player's guesses), 'foundAllLetters' is set to FALSE
            if secretWord[i] not in correctLetters:
                foundAllLetters = False
                break
        if foundAllLetters:
            print('Yes! The secret word is "' + secretWord + '"! You have won!')
            gameIsDone = True

    # If the player enters a letter that is NOT a letter in the secretWord, this code block executes (e.g. an incorrect guess)
    else:
        # Wrongly guessed letters are concatenated to the missedLetters string
        missedLetters = missedLetters + guess

        # Check if player has guessed too many times and lost
        # The HANGMANPICS list has 7 ASCII art strings.
        # When len(missedLetters) equals 6, you know the player has lost because the hangman picture will be finished.
        #   Remember, HANGMANPICS[0] is the first item in the list, and HANGMANPICS[6] is the last one.
        # Thus, when the length of the missedLetters string is equal to len(HANGMANPICS) - 1 (that is, 6), the player has run out of guesses.
        if len(missedLetters) == len(HANGMANPICS) - 1:
            displayBoard(HANGMANPICS, missedLetters, correctLetters, secretWord)
            print('You have run out of guesses!\nAfter ' + str(len(missedLetters)) + ' missed guesses and ' + str(
                len(correctLetters)) + ' correct guesses, the word was "' + secretWord + '"')
            gameIsDone = True

    # Ask the player if they want to play again (but only if the game is done).
    if gameIsDone:  # If 'gameIsDone' = TRUE
        if playAgain():  # And player wants to play another game ('y')
            missedLetters = ''  # Reset the missed and correct letters
            correctLetters = ''
            gameIsDone = False  # Switch the game state
            secretWord = getRandomWord(words)  # And get another word from the word list
        else:
            break  # If player declines, terminate session
