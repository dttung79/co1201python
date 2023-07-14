print('Welcome to the Grocery Store!')
print('Enter the item you want to buy (press Enter to finish)')

n_items = 1
entering = True
items = []

while entering:
    item = input(f'Item {n_items}: ')
    if item == '':
        entering = False
    else:
        n_items += 1
        items.append(item)

choice = input('Which items? (all/index): ')
if choice == 'all':
    print(items)
else:
    index = int(choice) - 1
    if index < -len(items) or index >= len(items):
        print('Invalid index')
    else:
        print(items[index])