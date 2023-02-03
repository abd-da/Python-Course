tuple1 = "Aboud",
print(tuple1)
print(type(tuple1))

tuple2 = 'Osama', 'Sami', 'Hadi'
x = tuple2
y = list(x)
y[0] = 'Elzero'
x = tuple(y)
print(x)
print(type(x))
print(f'{len(x)} Elements')

tuple3 = (1, 2, 3)
tuple4 = ('A', 'B', 'C')
tuple5 = tuple3 + tuple4
print(tuple5)
print(f'{len(tuple5)} Elements')

my_tuple = ("a", "b", "c", "d")
a, b, j, c = "a", "b", "c", "d"
print(a)
print(b)
print(c)
