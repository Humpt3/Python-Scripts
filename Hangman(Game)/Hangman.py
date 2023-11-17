
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
#DEFINICION DE VARIABLES Y LISTAS:

word_list = ["algeria", "argentina", "armenia", "russia", "chad", "england", "chile", "peru", "paraguay", "italy", "brasil", "canada", "guatemala", "mexico", "peru", "bolivia", "uruguay"] #Creo una lista con palabras aleatorias
display = [] # creo una lista vacia
lives = 6
end_game = False
chosen_word = random.choice(word_list) # eligo una palabra aleatoria de la lista creada word_list
chosen = list(chosen_word) # transformo la palabra elegida en una lista de caractéres para utilizar posteriormente

#print(chosen)
for letter in chosen_word:  #en este for agrego tantos elementos a la lista como letras tiene la palabra elegida aleatoriamente
    display.append("_")

print(display) # imprimo la lista con la cantidad de caracteres segun letras tenga la palabra

#print(chosen_word)
while end_game == False:

    guess = input("type a letter: ").lower()

    for i in range(0,len(chosen_word)):
        if chosen_word[i] == guess:
            display[i] = chosen_word[i]


    if guess not in chosen_word:
        lives = lives - 1
        print(f'Current lives: {lives}')
        print(stages[lives])
        if lives == 0:
            print("You lose")
            end_game = True

    print(display)

    if display == chosen:
       print("You win")
       end_game = True



'''i = 0 # creo una variable i que utilizaré como índice para el arreglo y la inicializo en cero.
for letter in chosen_word: #
    if guess == letter:
        display[i] = letter # si la letra escrita pertenece a la palabra elegida aleatoriamente, reemplazara el simbolo _ por la letra en cuestion en su respectivo índice
    i = i + 1'''

