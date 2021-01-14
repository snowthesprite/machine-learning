def show_board(locations) :
    board = [['.' for _ in range(8)] for __ in range(8)]
    index = 0
    while index < 8 :
        for row_index in range(8) :
            if row_index == locations[index][0] :
                for col_index in range(8) :
                    if col_index == locations[index][1] :
                        board[row_index][col_index] = str(index)
        index += 1
    for row_array in board :
        row_string = '  '.join(row_array)
        print(row_string)

def calc_cost(locations) : 
    hits = 0
    for queen in locations :
        for direction in range(4) :
            for opposing_queen in locations :
                if direction == 0 : #Up and Down
                    test_point = [0, queen[1]]
                    while test_point[0] < 8 :
                        if tuple(test_point) == opposing_queen and opposing_queen != queen :
                            hits += 1
                        test_point[0] += 1
                elif direction == 2 : #Left and right
                    test_point = [queen[0], 0]
                    while test_point[1] < 8 :
                        if tuple(test_point) == opposing_queen and opposing_queen != queen :
                            hits += 1
                        test_point[1] += 1
                elif direction == 3 : #top left to bottom right
                    test_point = list(queen)
                    while test_point[0] > 0 and test_point[1] > 0 : #top left
                        test_point[0] -= 1
                        test_point[1] -= 1
                        if tuple(test_point) == opposing_queen :
                            hits += 1
                    while test_point[0] < 8 and test_point[1] < 8 : #bottom right
                        test_point[0] += 1
                        test_point[1] += 1
                        if tuple(test_point) == opposing_queen :
                            hits += 1
                    elif direction == 3 : #top right to bottom left
                    test_point = list(queen)
                    while test_point[0] > 0 and test_point[1] > 0 : #top right
                        test_point[0] -= 1
                        test_point[1] -= 1
                        if tuple(test_point) == opposing_queen :
                            hits += 1
                    while test_point[0] < 8 and test_point[1] < 8 : #bottom left
                        test_point[0] += 1
                        test_point[1] += 1
                        if tuple(test_point) == opposing_queen :
                            hits += 1
    print(hits)


                       


locations = [(0,0), (6,1), (2,2), (5,3), (4,4), (7,5), (1,6), (2,6)]
print('The board')
print()
show_board(locations)
print()
calc_cost(locations)