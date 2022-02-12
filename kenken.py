grid_size = 9
key_list = []
value_list = [i+1 for i in range(grid_size)]

alphabet = [chr(i) for i in range(ord('a'), ord('a') + grid_size)]
for letter in alphabet:
    for num in value_list:
        square_label = letter + str(num)
        key_list.append(square_label)

kenken_grid = dict.fromkeys(key_list, value_list)

#print(kenken_grid)

print(kenken_grid['d3'])