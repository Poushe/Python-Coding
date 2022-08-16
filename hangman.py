#Step 1 
import random
stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
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
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']
word_list = ["ardvark", "baboon", "camel"]
d=random.choice(word_list)
len_d=len(d)
blank_list=[]
life=6
for j in d:
  blank_list+='_'
print(blank_list)
game_end= False
while not game_end:
  guess=input('Guess a letter:').lower()
  for i in range(0,len_d):
    if(d[i]==guess):
      blank_list[i]=guess
  print(blank_list)
  if "_" not in blank_list:
    game_end = True
    print('You Win')
  if guess not in d:
    life-=1
    print(stages[life])
    if life==0:
      game_end=True
      print('You Loss')
#TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.

#TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.

#TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word.
