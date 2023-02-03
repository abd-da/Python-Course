friendsList = ['Saadoun', 'Tony', 'Souad', 'Saeed', 'Eid']
print(friendsList[1])
print(friendsList[-4])
print(friendsList[0])
print(friendsList[-5])

print(friendsList.pop(1))
print(friendsList)

print(friendsList[1:4])
print(friendsList[-2:])

friendsList[-2:] = ['Elzero', 'Elzero']
print(friendsList)

b = "Mustafa"
c = 'Abdulrahman'
friendsList.insert(0, b)
print(friendsList)
friendsList.append(c)
print(friendsList)

del friendsList[0:2]
print(friendsList)
del friendsList[-1]
print(friendsList)

friendsList_2 = ['Humam', 'Hiba']
friendsList_3 = ['Aya', 'Durgham']
friendsList.extend(friendsList_2)
friendsList.extend(friendsList_3)
print(friendsList)

friendsList.sort()
print(friendsList)
friendsList.sort(reverse=True)
print(friendsList)

print(len(friendsList))

techs = ['CSS', 'JS', 'Python', 'Html']
frames = ['Flask', 'Web', 'Django']

techs.append(frames)
print(techs)
print(techs[4][2])
print(techs[4][1])