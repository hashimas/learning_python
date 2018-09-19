list = [1,2,3,4,5,6,7,8,9,10]
print('Original List = ',list)
list.append(11)
print('New List after appended ',list)
print(list[2:5])
print(list[2:])
print(list[:2])
x = list[:]
x.insert(len(x) +1,4)
print('x after insertion= ',x)
x.remove(x[len(x) - 1])
print('x after removing the inserted value = ',x)
