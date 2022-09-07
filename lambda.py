# Square
myList = [1, 2, 3, 4, 5, 6, 7]
print(list(map(lambda li: li ** 2, myList)))

# List Sorting
a = [(0, 2), (4, 3), (9, 9), (10, -1)]
a.sort(key=lambda x: x[1])
print(a)
