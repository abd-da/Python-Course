list = [1,5,4,3,3,2,1]
unique_list = set(list)
print(unique_list)
unique_list = [set(list)]
print(type(unique_list))
unique_list = set(list)
unique_list.discard(5)
print(unique_list)

print("=" * 50)

set1 = {1,2,3}
set2 = {'A','B','C'}
print(set1 | set2)
print(set1.union(set2))
set1.update(set2)
print(set1)

print("=" * 50)

S1 = {1,2,3}
print(S1)
S1.clear()
print(S1)
S1.add('A')
S1.add('B')
print(S1)

print("=" * 50)

S2 = {1,2,3}
S3 = {1,2,3,4,5,6}
print(S3.issuperset(S2))

print("=" * 50)

dictionary = {
    1 : {
        'name': 'HTML',
        'progress' : '90%'
    },
    2 : {
        'name': 'CSS',
        'progress': '80%'
    },
    3 : {
        'name': 'Python',
        'progress': '30%'
    }
}
print(dictionary[1])
print(dictionary[2])
print(dictionary[3])
dictionary[4] = 'AI progress is 20%'
print(dictionary[4])