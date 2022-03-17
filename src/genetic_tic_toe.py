import random
#and tic-tac-toe...
class GeneticAlgorithm () :
    def __init__(self, num_players) :
        self.pop_size = num_players
        self.original_gen = self.create_players(num_players)
        self.good_moves = self.state_freq()

    def get_possible_moves(self, game_state) :
        possible_moves = []
        if self.check_for_winner(game_state) != None :
            return [[]]
        for index in range(len(game_state)) :
            if game_state[index] == '0':
                possible_moves.append(index)
        if possible_moves == [] :
            possible_moves.append([])
        return possible_moves

    def state_freq(self) : 
        states = {}
        for state in self.original_gen[0] :
            if state.count('2') < 2 :
                continue
            if state.count('1') == state.count('2') :
                sym = 1
            else :
                sym = 2
            chance = {}
            good_moves = self.catagorize_moves(state, sym)
            chance['win_moves'] = organized_moves[0]
            chance['block_moves'] = organized_moves[1]
            states[state] = chance
        return states
            
    def catagorize_moves(self, state, sym) :
        win_moves = []
        loose_moves = []
        for move in self.get_possible_moves(state) :
            board = state.copy()
            board[move] = str(sym)
            if self.check_for_winner(board) == sym :
                win_moves.append(move)
            elif self.check_for_winner(board) == (sym % 2)+1 :
                loose_moves.append(move)
        return [win_moves, loose_moves]

    def create_players(self) :
        players = [{} for _ in range(self.pop_size)]
        prev_choices = ['000000000']
        num = 1
        while prev_choices != [] :
            choice = prev_choices[0]
            possible_choices = self.get_possible_moves(choice)
            if [] in possible_choices :
                prev_choices.remove(choice)
                continue
            for player in players :
                player[choice] = random.choice(possible_choices)
            update = [choice[:value] + str(num) + choice[value+1:] for value in possible_choices]
            prev_choices.remove(choice)
            prev_choices.extend([move for move in update if move not in prev_choices])
            num = (num % 2) + 1
        return players

    def find_player_scores(self, group_1, group_2) :
        plr_score = [{index : 0 for index in range(self.pop_size)} for _ in range(2)]
        for plr_1 in range(self.pop_size) :
            for plr_2 in range(self.pop_size) :
                game = TicTacToe([group_1[plr_1], group_2[plr_2]])
                if game.winner == 1 :
                    plr_score[plr_1] += 1
                    plr_score[plr_2] -= 1
                elif game.winner == 2 :
                    plr_score[plr_1] -= 1
                    plr_score[plr_2] += 1
        return plr_score

    def find_plr_scores_same(self, group) :
        plr_score = {index : 0 for index in range(len(group))}
        for plr_1 in range(self.pop_size) :
            for plr_2 in range(self.pop_size) :
                if plr_1 == plr_2 :
                    continue
                game = TicTacToe([group[plr_1], group[plr_2]])
                if game.winner == 1 :
                    plr_score[plr_1] += 1
                    plr_score[plr_2] -= 1
                elif game.winner == 2 :
                    plr_score[plr_1] -= 1
                    plr_score[plr_2] += 1
        return plr_score
    
    def find_top_5(self, group) :
        scores = self.find_plr_scores_same(group)
        scores = [score for score in scores.items()]
        scores.sort(reverse=True, key=(lambda x : x[1]))
        return [group[id] for id, score in scores[:5]]

    def mate(self, group) :
        children = []
        for mom_1 in range(len(group)) :
            for mom_2 in range(mom_1+1, len(group)) :
                kids = [{},{}]
                for state in group[mom_1] :
                    kids[0][state] = group[random.choice([mom_1,mom_2])][state]
                    kids[1][state] = group[random.choice([mom_1,mom_2])][state]
                children.extend(kids)
        return children

    def for_generation(self, gen) :
        wanted_data = {}
        current_gen = self.original_gen
        for generation in range(gen) :
            top = self.find_top_5(current_gen)
            next_gen = self.mate(top)
            next_gen.extend(top)

    def run_game(self, players) :
        index = 1
        winner = None
        board = ['0' for _ in range(9)]
        while winner == None :
            plr = players[index]
            choice = plr[''.join(board)]
            if choice != [] :
                board[choice] = str(index)

            winner = self.check_for_winner()
            index = (index % 2) + 1
        return winner

    def organize_board(self, board) :
        board = ''.join(board)

        thing = [board[index: index+3] for index in range(0,9,3)] #row
        for index in range(3) :
            thing.append([board[index] + board[index+3] + board[index+6]]) #column
        thing.extend([[board[0] + board[4] + board[8]], [board[2] + board[4] + board[6]]]) #diagonal
        return thing

    def check_for_winner(self, board) :
        thing = self.organize_board(board)
        for stuff in thing :
            if len(set(stuff)) == 1 and set(stuff) != {'0'} :
                return int(stuff[0])
        if '0' not in board :
            return 'tie'
                