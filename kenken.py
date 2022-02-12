grid_size = 5
info1 = [['a1', 'b1', 'a2'], ['a3', 'a4'], ['a5', 'b5'], ['b2', 'c2'], ['b3', 'c3'], ['b4', 'c4'], ['c1', 'd1'], ['c5', 'd5'], ['d2', 'd3'], ['d4'], ['e1', 'e2', 'e3'], ['e4', 'e5']]
info2 = [48, 3, 4, 8, 10, 4, 3, 2, 4, 4, 7, 15]
info3 = ['*', '+', '-', '+', '*', '+', '-', '/', '+', 'n', '+', '*']
#info4 = [False] * len(info2)
square_groups = list(zip(info1, info2, info3))

group = 0
constaint_num = 1
operation = 2

#print(data)

square_list = []
possible_answers_list = [i+1 for i in range(grid_size)]

alphabet = [chr(i) for i in range(ord('a'), ord('a') + grid_size)]
for letter in alphabet:
    for num in possible_answers_list:
        square_label = letter + str(num)
        square_list.append(square_label)

kenken_grid = dict.fromkeys(square_list, [])
kenken_grid['a4'].append(1)
print(kenken_grid)



def update_row_and_col(square, answer):
    print(kenken_grid)
    for sq in kenken_grid.keys():
        print(sq)
        print(kenken_grid[sq])
        if (square[:1] in sq or square[1:] in sq) and sq != square:
            print(kenken_grid[sq])
            (kenken_grid[sq]).remove(answer)
            print(kenken_grid[sq])
        print(kenken_grid)


def update_grid(squares, answers):
    for s in squares:
        kenken_grid[s] = answers
    
    for sq, ans in kenken_grid.items():
        if len(ans) == 1:
            update_row_and_col(sq, ans[0])
            
#print(key[:1])


for i in range(len(square_groups) - 1):
    if len(square_groups[i][group]) == 1:
        possible_answers = [square_groups[i][constaint_num]]
        update_grid(square_groups[i][group], possible_answers)
        square_groups.pop(i)

print(kenken_grid)
#print(square_groups)
