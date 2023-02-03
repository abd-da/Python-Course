name = input('What do they call ya?')
print(f'Hello {name.strip().capitalize()}, happy to see you here!')

age = int(input('How old are ya?').strip())
if age >= 16:
    print(f'Hello {name.strip().capitalize()}, happy to see you here!All Articles Is Suitable For You')
else:
    print(f'Hello {name.strip().capitalize()}, Your Age Is Under 16, Some Articles Is Not Suitable For You')


first_name = input('What is your first name?')
last_name = input('What is your last name?')
print(f'Hello {first_name.strip().capitalize()} {last_name[0].strip().capitalize()}')

email = input('What is your email?').strip().lower()
print('Your username is ' + email[:email.index('@')].capitalize())
print('Your sp is ' + email[email.index('@'):email.index('.')])
print('Your tld is ' + email[email.index('.'):])