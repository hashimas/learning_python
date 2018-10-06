a = [2,3,4,5]
b = [4,5,7,8]
c = [3,4,5,6]
d = [a,b,c]
#print([[row[i] for row in d] for i in range(4)])
transposed = []
for i in range(4):
    transposed.append([row[i] for row in d])
print(transposed)