
import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

n_letter = int(input("How many letters would you like in your password? "))
n_symbol= int(input("How many symbols would you like? "))
n_number = int(input("How many numbers would you like ?"))

password = []

for char in range(1,n_letter+1):
    random_char = random.choice(letters)
    password.append(random_char)

for sym in range(1,n_symbol+1):
    random_sym = random.choice(symbols)
    password.append(random_sym)

for num in range(1,n_number +1):
    random_num = random.choice(numbers)
    password.append(random_num)

print(password)
random.shuffle(password) # la funcion shuffle nos permite ordenar aleatoriamente una lista ya existente.
print(password) # como vemos nos devuelve la contraseña en forma de lista,pero para que se vea mejor debemos devolverla en forma de string, esto lo hacemos mediante un ciclo for

pas = ""
for elem in password:
    pas = pas + elem

print(f'The password Generated is: {pas}')