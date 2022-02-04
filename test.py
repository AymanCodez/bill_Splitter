import random


def split_bill(bill, num):
    split = round((bill / len(num)), 2)
    if split.is_integer():
        split = int(split)

    for key in num:
        num[key] = split

    return names


print('Enter the number of friends joining (including you): ')
number = int(input())
print()

if number <= 0:
    print('No one is joining for the party')
else:
    print('Enter the name of every friend (including you), each on a new line: ')
    names = {input(): 0 for i in range(number)}
    print()
    bill_amount = int(input('Enter the total bill value: '))
    print()

    split_dic = split_bill(bill_amount, names)

    answer = input('Do you want to use the "Who is lucky?" feature? Write Yes/No: ')

    if answer == 'Yes':
        lucky = random.choice(list(names.keys()))
        new_split = round((bill_amount / (len(names) - 1)), 2)
        if new_split.is_integer():
            new_split = int(new_split)

        for k, v in names.items():
            if not names[k] == lucky:
                names[k] = new_split
        names[lucky] = 0

        print()
        print(f'{lucky} is the lucky one!')
        print()
        print(names)
    elif answer == 'No':
        print()
        print('No one is going to be lucky')
        print()
        print(names)
