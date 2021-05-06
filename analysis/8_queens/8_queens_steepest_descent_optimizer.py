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
    return point_1[1] == point_2[1]

def on_row(point_1, point_2) :
    return point_1[0] == point_2[0]

def on_diagonal(point_1, point_2) :
    slope = (point_2[0] - point_1[0]) / (point_2[1] - point_1[1])
    return slope == 1 or slope == -1 #I think that works

def calc_cost(locations) : 
    hits = 0
    for queen in locations :
        for opposing_queen in locations :
            if queen != opposing_queen :
                if on_row(queen, opposing_queen):
                    hits += 1
                elif on_col(queen, opposing_queen):
                    hits += 1
                elif on_diagonal(queen, opposing_queen) :
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

def changed_locations(point) :
    x = point[0]
    y = point[1]
    return [(x+1,y), (x+1,y+1), (x+1,y-1), (x,y-1), (x,y+1), (x-1,y-1), (x-1,y), (x-1,y+1)]

def steepest_descent_optimizer(n) :
    current = random_optimizer(100)
    current_location = current['locations']
    current_cost = current['cost']
    for _ in range(n) : 
        for queen_index in range(8) :
            queen = current_location[queen_index]
            new_spots = changed_locations(queen)
            for spot in new_spots :
                if spot in current_location or spot[0] < 0 or spot[1] < 0 or spot[0] > 7 or spot[1] > 7 :
                    continue
                possible_location = current_location.copy()
                possible_location[queen_index] = spot
                possible_cost = calc_cost(possible_location)
                if possible_cost < current_cost :
                    current_cost = possible_cost
                    current_location = possible_location
        if current_cost == 0 :
            break
    return {'locations' : current_location, 'cost' : current_cost}

print('n = 10', steepest_descent_optimizer(10), "\n")

print('n = 50', steepest_descent_optimizer(50), "\n")

print('n = 100', steepest_descent_optimizer(100), "\n")

print('n = 500', steepest_descent_optimizer(500), "\n")

print('n = 1000', steepest_descent_optimizer(1000), "\n")