print('Welcome to the party!')
n_guests = int(input('How many guests will be attending?'))

guests = [''] * n_guests

for i in range(n_guests):
    name = input(f'Enter the name of guest {i+1}: ')
    guests[i] = name

print('The final guest list is: ', guests)

choice = input('Do you want to remove any guests? (yes/no): ')

if choice == 'yes':
    name = input('Enter the name of the guest to remove: ')
    if name in guests:
        guests.remove(name)
        print('The updated guest list is: ', guests)
    else:
        print('That guest is not in the list')