number = int(input("Please enter an odd number: "))
while number%2==0:
    number = int(input("Please enter an odd number: "))
for i in reversed(list(range(number))):
    print((' ' * ( number- i - 1 ) + '*' * ( 2 * i + 1)))
