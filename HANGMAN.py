#Step 1 
import hangman_words

#TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.

#TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.

#TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word.
import random
print("Let's play Hangman!")
print("This is your word:")

chosen_word= random.choice(hangaman_words.word_list)
chosen_word_list=list(chosen_word)
spaces=""
for n in chosen_word:
  spaces+="_"
print(spaces)
spaces_list=list(spaces)


lives=len(chosen_word)
n=""
guess=input("Guess a letter: ").lower()
while lives>0 and (guess != chosen_word):
  
  if guess in chosen_word:
    lives+=0
    def get_indices(element, lst):
      return [i for i, x in enumerate(lst) if x == element]
    indices=get_indices(guess,chosen_word)
    
    for i in indices:
      spaces_list[i]=guess
    
    currentwordspaces=' '.join(spaces_list)
    def remove(string):
      return string.replace(" ", "")
    guess=remove(currentwordspaces)
    
    if not guess==chosen_word:
      print("You guessed a letter!")
      print(guess)
      guess=input("Guess a letter: ").lower()
    else:
      print("You guessed the word!")
      print(guess)
      print("You win!")
        
      
  if not guess in chosen_word:
    lives-=1
    print(f"You are wrong...You have {lives} lives left")
    guess=input("Guess a letter: ").lower()

    
else:
  print("Game Over!")
  
