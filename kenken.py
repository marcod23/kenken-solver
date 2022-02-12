grid_size = 4
info1 = [['a1', 'b1'], ['a2', 'b2']]
info2 = [5, 2]
info3 = ['+', '/']
data = list(zip(info1, info2, info3))
print(data)
print(data[1][2])
print(data[1][0][1])
print(type(data[0][1]))

key_list = []
value_list = [i+1 for i in range(grid_size)]

alphabet = [chr(i) for i in range(ord('a'), ord('a') + grid_size)]
for letter in alphabet:
    for num in value_list:
        square_label = letter + str(num)
        key_list.append(square_label)

kenken_grid = dict.fromkeys(key_list, value_list)

#print(kenken_grid)

#print(kenken_grid['d3'])