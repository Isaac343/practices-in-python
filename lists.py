w = int(input('height: '))
h = int(input('weight: '))
data = []
multi = [1, 2, 3]
for a in range(w):
    data.append([])
    for b in range(h):
        value = int(input('insert value: '))
        data[a].append(value)
print(data)
