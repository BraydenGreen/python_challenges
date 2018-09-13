number = int(input("Please input an integer: "))
if number < 0:
    number = 0
    print('Negative changed to zero')
elif number == 0:
    print('Zero')
elif number == 1:
    print('One')
else:
    print('More')
