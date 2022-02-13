import itertools
import numpy as np

OPERATIONS = {
        '+': np.add,
        '-': np.subtract,
        '*': np.multiply,
        '/': np.divide,
}



grid_size = 5
info1 = [['a1', 'b1', 'a2'], ['a3', 'a4'], ['a5', 'b5'], ['b2', 'c2'], ['b3', 'c3'], ['b4', 'c4'], ['c1', 'd1'], ['c5', 'd5'], ['d2', 'd3'], ['d4'], ['e1', 'e2', 'e3'], ['e4', 'e5']]
info2 = [48, 3, 4, 8, 10, 4, 3, 2, 4, 4, 7, 15]
info3 = ['*', '+', '-', '+', '*', '+', '-', '/', '+', 'n', '+', '*']
#info4 = [False] * len(info2)
grid_groups = list(zip(info1, info2, info3))

# each square will be labeled with a letter corresponding to the row it's in and a
# number for the column it's in
square_labels = []
letters = [chr(i) for i in range(ord('a'), ord('a') + grid_size)]
numbers = [i+1 for i in range(grid_size)]
for letter in letters:
    for num in numbers:
        square_label = letter + str(num)
        square_labels.append(square_label)

kenken_grid = dict.fromkeys(square_labels, [])
# need to do this to make sure that each key has a unique answer list that can be altered
for k in kenken_grid:
    initial_possible_answers = [i+1 for i in range(grid_size)]
    kenken_grid[k] = initial_possible_answers



def update_row_and_col(square, answer):
    for sq in kenken_grid.keys():
        if (square[:1] in sq or square[1:] in sq) and sq != square:
            (kenken_grid[sq]).remove(answer)


def update_grid(squares, answers):
    for s in squares:
        kenken_grid[s] = answers
    
    for sq, ans in kenken_grid.items():
        if len(ans) == 1:
            update_row_and_col(sq, ans[0])


def grid_group_math(group, constraint_num, operation):
    group_numbers = [1, 2, 3, 4, 5]
    group_numbers1 = [5, 4, 3, 2, 1]
    for combination in itertools.combinations_with_replacement(group_numbers1, len(group)):
        if OPERATIONS[operation].reduce(combination, dtype=float) == constraint_num:
            print(combination)
    



for i in range(len(grid_groups) - 1):

    group = grid_groups[i][0]
    print(group)
    constraint_num = grid_groups[i][1]
    operation = grid_groups[i][2]
    
    if len(group) == 1:
        possible_answers = [constraint_num]
        update_grid(group, possible_answers)
    else:
        grid_group_math(group, constraint_num, operation)



#print(kenken_grid)
print(grid_groups)
