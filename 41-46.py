x = int(input('num1:').strip())
y = int(input('num2:').strip())
operation = input("Please enter one of the values '+' or '-' or '*' or '/' or '%'").strip()
if operation == '+':
    print(x + y)
elif operation == '-':
    print(x - y)
elif operation == '*':
    print(x * y)
elif operation == '/':
    print(x / y)
elif operation == '%':
    print(x % y)
else:
    print('Please enter one of the following values: + - * / %')

age = 17
if age >= 16: print('App Is Suitable For You')
else: print('App Is Not Suitable For You')

age1 = int(input('How old are you?'))
if age1 >= 100:
    print('Sorry, you are dying soon.')
elif 10 < age1 < 100:
    print(f'You age is: {age1 * 12} Months')
    print(f'You age is: {age1 * 52} Weeks')
    print(f'You age is: {age1 * 365} Days')
    print(f'You age is: {age1 * 8760} Hours')
    print(f'You age is: {age1 * 525600} Minutes')
    print(f'You age is: {age1 * 31536000} Seconds')
else:
    print('Go study, kiddo.')

country = input("Input Your Country: ").capitalize().strip()
a_countries = ["Egypt", "Palestine", "Syria", "Yemen", "KSA", "Bahrain"]
na_countries = ["USA", "England"]
price = 100
discount = 30
if country.capitalize() not in a_countries and not na_countries:
    print('Please enter a valid choice.')
elif country.capitalize() in a_countries:
    print(f'Congrats! Your are eligible for a discount. And your item is {price - discount}$')
elif country.capitalize() in na_countries:
    print(f'Your item is {price}$')