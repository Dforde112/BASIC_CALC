#BASIC CALCULATOR

while True:
    first_number =float(input('1st number > '))
    second_number =float(input('2nd number > '))
    user_input = input('what do you want to do with these numbers?\n+ - add\n- - subtract\nx - multiply\n/ - divide\n')
    if user_input == '+':
        print(first_number + second_number)
    elif user_input == '-':
        print(first_number - second_number)
    elif user_input == '/':
        print(first_number/second_number)
    elif user_input == 'x':
        print(first_number * second_number)
    else:
        print('Looks like something went wrong! Try again.')