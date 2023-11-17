'''


program that tells us how many days, weeks, months we have left if we live until 90 years old.

It will take your current age as the input and output a message with our time left in this format:

You have x days, y weeks, and z months left.

Where x, y and z are replaced with the actual calculated numbers.

'''

currentAge = int(input("Please type your current age: "))
diedAge = 90
x = (diedAge * 365) - (currentAge * 365)
y = (diedAge * 52) - (currentAge * 52)
z = (diedAge * 12) - (currentAge * 12)

print(f'You have {x} days, {y} weeks, and {z} months left.')

