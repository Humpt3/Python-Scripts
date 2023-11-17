#Writting the main functions of the calculator
#Add
def add(n1, n2):
    return n1+n2
#Substract
def substract(n1, n2):
    return n1-n2

#Multiply
def multiply(n1,n2):
    return n1*n2

#Divide
def divide(n1, n2):
    return n1/n2

operations = {
    "+" : add,
    "-" : substract,
    "*" : multiply,
    "/" : divide
}
num1 = int(input("write the first number: "))
num2 = int(input("write a seccond number: "))

for symbol in operations: #recorriendo el diccionario
    print(symbol) # De esta forma imprimo todas las key, si quisiera además imprimir los valores deberia hacer un print(operation[op])
op_symbol = input("Pick an operation: ")
for symbol in operations:
    if op_symbol == symbol:
        function = operations[op_symbol]



print(f'The result is: {function(num1,num2)}')
# function = operations["+"]
# print(function(2,3))