

bill = float(input("Type the total of the bill: "))
people = int(input("Type the number of people that are going to pay for the bill: "))

total_bill = bill * 0.12 + bill
total_people = total_bill / people

print(f'Each person should pay: {format(total_people,".2f")}')
