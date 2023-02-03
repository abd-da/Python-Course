print(bool(100 > 50))
print(bool(50 == 50))
print(bool(100 != 40))
print(bool(5 != 10))
print(bool(50 > 50))
print(bool(5 > 10))
print(bool(False))
print(bool())

print('=' * 40)

html = 80
css = 60
javascript = 70
print(bool(html > 50 and javascript > 50 and css > 50))

print('=' * 40)

num_one = 10
num_two = 20
num = 20
print(bool(num > num_one or num > num_two))
print(bool(num > num_one and num > num_two))

print('=' * 40)

num_one = 10
num_two = 20
print(num_one + num_two)
print((num_one + num_two)**3)
print(int(((num_one + num_two)**3)/26000))
print(float(int(((num_one + num_two)**3)/26000))/5)
print(type(str(float(int(((num_one + num_two)**3)/26000))/5)))