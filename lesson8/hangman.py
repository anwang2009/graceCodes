# Problem Set 2, hangman.py
# Name: An and Grace
# Collaborators: Us
# Time spent: ~2.5 hours

# Hangman Game
# -----------------------------------
import random
import string
WORDLIST_FILENAME = "words.txt"

def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist


def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)
    
    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

wordlist = load_words()

def is_word_guessed(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing; assumes all letters are
      lowercase
    letters_guessed: list (of letters), which letters have been guessed so far;
      assumes that all letters are lowercase
    returns: boolean, True if all the letters of secret_word are in letters_guessed;
      False otherwise
    '''
    for i in range(len(secret_word)):
      if secret_word[i] not in letters_guessed:
         return False
    return True


def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents
      which letters in secret_word have been guessed so far.
    '''
    result = ""
    for i in range(len(secret_word)):
      if secret_word[i] in letters_guessed:
        result += secret_word[i]
      else:
        result += "_"
    print(result)
    return result
        


def get_available_letters(letters_guessed):
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    '''
    give = ""
    alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    for i in range(26):
       if alphabet[i] not in letters_guessed:
          give += alphabet[i]
    return give
          
def hangman(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses

    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Remember to make
      sure that the user puts in a letter!
    
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
    
    Follows the other limitations detailed in the problem write-up.
    '''
    guess = 6
    print("Secret word length:", len(secret_word))
    print("You have 6 guesses!")
    letters_guessed = []
    while guess > 0:
      letter = input("Please guess a letter:")
      letters_guessed.append(letter)
      if letter in secret_word:
        print("Great! :) Your current state of being of the word is", get_guessed_word(secret_word, letters_guessed))
        if is_word_guessed(secret_word, letters_guessed):
           print("Great job! You are amazing.")
           break
      else:
        print("Oops! :( Your current state of being of the word is", get_guessed_word(secret_word, letters_guessed))
        guess -= 1

      print("Here are the available letters:", get_available_letters(letters_guessed))
      print("You have", guess, "guesses left!")

    print("GAME OVER!")        
if __name__ == "__main__":
    secret_word = choose_word(wordlist)
    hangman(secret_word)