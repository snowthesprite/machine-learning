import random
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

def on_col(point_1, point_2) :
    test_point = [0, point_1[1]]
    while test_point[0] < 8 :
        if tuple(test_point) == point_2 :
            return True
        test_point[0] += 1
    return False

def on_row(point_1, point_2) :
    test_point = [point_1[0], 0]
    while test_point[0] < 8 :
        if tuple(test_point) == point_2 :
            return True
        test_point[1] += 1
    return False

def on_diagonal(point_1, point_2) :
    slope = (point_2[1] - point_1[1]) / (point_2[0] - point_1[1])
    if slope == 1 or slope == -1 :
        return True
    return False

def calc_cost(locations) : 
    hits = 0
    for queen in locations :
        for opposing_queen in locations :
            if queen != opposing_queen :
                row_test = on_row(queen, opposing_queen)
                col_test = on_col(queen, opposing_queen)
                diagonal_test = on_diagonal(queen, opposing_queen)
                if row_test or col_test or diagonal_test :
                    hits += 1
    return hits / 2

def random_optimizer(n) :
    all_locations = [[] for _ in range(n)]
    for location_index in range(n) :
        for queen in range(8) :
            queen_location = (random.randint(0,8), random.randint(0,8))
            all_locations[location_index].append(queen_location)
    lowest_cost = calc_cost(all_locations[0])
    for location_set in all_locations :
        cost = calc_cost(location_set)
        if cost <= lowest_cost :
            lowest_cost = cost
            lowest_location = location_set
    return {'locations' : lowest_location, 'cost' : lowest_cost}
                       

locations = [(0,0), (6,1), (2,2), (5,3), (4,4), (7,5), (1,6), (2,6)]
print('The board')
print()
show_board(locations)
print()

print('Can calc_cost find all overlaps between queens?')
assert calc_cost(locations) == 10, 'No it can not'
print('Yes it can')

print(random_optimizer(5))