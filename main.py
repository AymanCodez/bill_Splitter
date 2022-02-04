# import random
#
#
# print('Enter the number of friends joining (including you): ')
# number = int(input())
# print()
#
# if number <= 0:
#     print('No one is joining for the party')
# else:
#     print('Enter the name of every friend (including you), each on a new line: ')
#     names = {input(): 0 for i in range(number)}
#     print()
#     bill = int(input('Enter the total bill value: '))
#     print()
#
#     split_bill = round((bill / len(names)), 2)
#     if split_bill.is_integer():
#         split_bill = int(split_bill)
#
#     for key in names:
#         names[key] = split_bill
#
#     answer = input('Do you want to use the "Who is lucky?" feature? Write Yes/No: ')
#     if answer == 'Yes':
#         lucky = random.choice(list(names.keys()))
#         print(f'{lucky} is the lucky one!')
#     elif answer == 'No':
#         print('No one is going to be lucky')
