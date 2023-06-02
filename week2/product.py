# Enter product information (name, price, stock) and print the information in a table

name = input('Enter product name: ')
price = float(input('Enter product price: '))
stock = int(input('Enter product stock: '))

print('+' + '-' * 20 + '+' + '-' * 10 + '+' + '-' * 10 + '+' + '-' * 10 + '+')
print(f'|{"Name":<20}|{"Price":>10}|{"Stock":>10}|{"Value":>10}|')
print('+' + '-' * 20 + '+' + '-' * 10 + '+' + '-' * 10 + '+' + '-' * 10 + '+')
print(f'|{name:<20}|{price:>10.2f}|{stock:>10}|{price * stock:>10.2f}|')
print('+' + '-' * 20 + '+' + '-' * 10 + '+' + '-' * 10 + '+' + '-' * 10 + '+')