first_name = 'Abdul'
age = '28'
country = 'Syria'
print('Hello ' + first_name + ', How are you doing \\ """ Your age is "' + age + '"" + Your country is: ' + country)
print('Hello ' + first_name + ', How are you doing \\')
print('""" Your age is "' + age + '"" +')
print('And your country is: ' + country)

name2 = 'Elzero'
print('Second letter is "' + name2[1] + '"')
print('Third letter is "' + name2[2] + '"')
print('Last letter is "' + name2[5] + '"')
print('"' + name2[1:4] + '"')
print('"' + name2[0::2] + '"')
print('"' + name2[-2] + name2[2:4] + '"')

a, b, c, d, e= "9", "15", "130", "950", "1500"
print(a.zfill(4))
print(b.zfill(4))
print(c.zfill(4))
print(d.zfill(4))
print(e.zfill(4))

name_one = "Mustafa"
name_two = "Tarek"

print(name_one.rjust(16, "@"))
print(name_two.rjust(9, "@"))

print(name_one.swapcase())
print(name_two.swapcase())

msg = "I Love Python And Although Love Elzero Web School"

print(msg.count("Love"))

print(name2.find("z"))

print(msg.replace("Love" , "<3", 1))
print(msg.replace("Love" , "<3"))

first_name2 = 'Bilal'
age2 = 28
country2 = 'Lebanon'

print(f"My Name is {first_name2}, and my age is {age2}, and my country is {country2}")
