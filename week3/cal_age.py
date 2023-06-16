current_year = 2023

birth_year = int(input("Enter your birth year: "))
if birth_year <= current_year and birth_year > 0:
    age = current_year - birth_year
    print('You are', age, ', years old.')
else:
    print('Invalid birth year')

print('Goodbye')
