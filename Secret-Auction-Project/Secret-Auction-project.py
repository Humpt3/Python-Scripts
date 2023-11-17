logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''

print(logo)
subastas = {}
def secretAuction(name, bid):
    subastas[name] = bid

def find_highest(dictionary):
    highest = 0
    for key in dictionary:
        bid_amount = dictionary[key]
        if bid_amount>highest:
            highest = bid_amount
            winner = key
    print(f'The winner is: {winner} and the highest bid is: {highest}')

ending = False


while ending == False:
    name = input("Insert a name: ")
    bid = int(input("Insert your bid price: "))
    secretAuction(name=name, bid=bid)
    op = input("Is there any other user who want to bid? | yes | no \n ")
    if op == "no":
        find_highest(dictionary=subastas)
        ending == True

