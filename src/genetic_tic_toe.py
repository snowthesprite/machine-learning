import random as rand
#and tic-tac-toe...
class GeneticAlgorithm () :
    def __init__(self, num_players, mut_rate=0) :
        self.pop_size = num_players
        self.mut_rate = mut_rate
        self.gen_0 = self.create_players()
        self.good_moves = self.state_freq()

    def get_possible_moves(self, game_state) :
        possible_moves = []
        thing = self.check_for_winner(game_state)
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
        for state in self.gen_0[0] :
            if state.count('2') < 2 :
                continue
            if state.count('1') == state.count('2') :
                sym = 1
            else :
                sym = 2
            chance = {}
            good_moves = self.catagorize_moves(state, sym)
            chance['win_moves'] = good_moves[0]
            chance['block_moves'] = good_moves[1]
            states[state] = chance
        return states
            
    def catagorize_moves(self, state, sym) :
        win_moves = []
        block_moves = []
        for move in self.get_possible_moves(state) :
            board = list(state)
            board[move] = str(sym)
            if self.check_for_winner(board) == sym :
                win_moves.append(move)
            board[move] = str((sym%2)+1)
            if self.check_for_winner(board) == (sym % 2)+1 :
                block_moves.append(move)
        return [win_moves, block_moves]

    def create_players(self) :
        players = [{} for _ in range(self.pop_size)]
        prev_choices = ['000000000']
        while prev_choices != [] :
            choice = prev_choices[0]
            prev_choices.remove(choice)
            possible_choices = self.get_possible_moves(choice)
            if [] in possible_choices :
                continue
            if choice.count('1') == choice.count('2') :
                sym = 1
            else :
                sym = 2
            for player in players :
                player[choice] = rand.choice(possible_choices)
            update = [choice[:value] + str(sym) + choice[value+1:] for value in possible_choices]
            prev_choices.extend([move for move in update if move not in prev_choices])
        return players

    def find_player_scores(self, group_1, group_2) :
        plr_score = [{index : 0 for index in range(self.pop_size)} for _ in range(2)]
        for plr_1 in range(self.pop_size) :
            for plr_2 in range(self.pop_size) :
                winner = self.run_game([group_1[plr_1], group_2[plr_2]])
                if winner == 1 :
                    plr_score[0][plr_1] += 1
                    plr_score[1][plr_2] -= 1
                elif winner == 2 :
                    plr_score[0][plr_1] -= 1
                    plr_score[1][plr_2] += 1
                winner = self.run_game([group_2[plr_2], group_1[plr_1]])
                if winner == 1 :
                    plr_score[0][plr_1] -= 1
                    plr_score[1][plr_2] += 1
                elif winner == 2 :
                    plr_score[0][plr_1] += 1
                    plr_score[1][plr_2] -= 1
        return plr_score
    

    #Change name on this, not right
    def hard_cutoff_RR(self, group) :
        plr_score = {index : 0 for index in range(len(group))}
        for plr_1 in range(len(group)) :
            for plr_2 in range(len(group)) :
                if plr_1 == plr_2 :
                    continue
                winner = self.run_game([group[plr_1], group[plr_2]])
                if winner == 1 :
                    plr_score[plr_1] += 1
                    plr_score[plr_2] -= 1
                elif winner == 2 :
                    plr_score[plr_1] -= 1
                    plr_score[plr_2] += 1
        return plr_score
    
    def find_top(self, group, num) :
        scores = self.hard_cutoff_RR(group)
        scores = [score for score in scores.items()]
        scores.sort(reverse=True, key=(lambda x : x[1]))
        #print(scores)
        return [group[id] for id, score in scores[:num]]

    def tournament_RR(self, group) :
        grup = group.copy()
        chosen = []
        while len(chosen) < self.pop_size/4 :
            round = []
            while len(round) < self.pop_size/8 :
                player = rand.choice(grup)
                if player in chosen  :
                    grup.remove(player)
                    continue
                elif player in round :
                    continue
                round.append(player)
            if len(grup) < self.pop_size/4 + self.pop_size/8 :
                return False
            best = self.find_top(round, 1)
            chosen.extend(best)
        return chosen
            
    def stochastic_RR(self, group) :
        grup = self.hard_cutoff(group)
        chosen = []
        while len(chosen) < self.pop_size/4 :
            round = []
            while len(round) < self.pop_size/8 :
                player = rand.choice(list(grup.items()))
                if player in chosen  :
                    grup.pop(player[0])
                    continue
                elif player in round :
                    continue
                round.append(player)
            if len(grup) < self.pop_size/4 + self.pop_size/8 :
                print('ran')
                return False
            round.sort(reverse=True, key=(lambda x : x[1]))
            chosen.append(round[0])
        return [group[id] for id, score in chosen]

    def avg_score(self, group_1, group_2) :
        scores = self.find_player_scores(group_1, group_2)
        g_1_score = [score for score in scores[0].values()]
        #print(sum(g_1_score)/len(g_1_score))
        return sum(g_1_score)/len(g_1_score)
    '''
    def mate(self, group) :
        children = []
        for mom_1 in range(len(group)) :
            for mom_2 in range(mom_1+1, len(group)) :
                kids = [{},{}]
                for state in group[mom_1] :
                    kids[0][state] = group[rand.choice([mom_1,mom_2])][state]
                    kids[1][state] = group[rand.choice([mom_1,mom_2])][state]
                children.extend(kids)
        return children
    '''
    def mate(self, group) :
        children = []
        while len(children) + len(group) < self.pop_size :
            mom_1 = rand.choice(group)
            mom_2 = rand.choice(group)
            kid = {}
            for state in mom_1 :
                options = [mom_1[state], mom_2[state], rand.choice(self.get_possible_moves(state))]
                kid[state] = rand.choices(options,weights=((1-self.mut_rate)/2, (1-self.mut_rate)/2, self.mut_rate),k=1)
            children.append(kid)
        return children

    def bracket (self, group) :
        bracket = {0: group.copy()}
        current_round = 0
        while len(bracket[current_round]) > 1 :
            tier = bracket[current_round]
            winners = []
            loosers = []
            while len(tier) != len(winners) :
                round = []
                while len(round) < 2 :
                    player = rand.choice(tier)
                    if player in round or player in loosers:
                        continue
                    round.append(player)
                game = self.run_game(round) 
                if game == 'tie' :
                    game = 0
                else :
                    game = int(game)-1
                winners.append(round[game])
                tier.remove(round[game])
                loosers.append(round[(game+1)%2])
            current_round += 1
            bracket[current_round] = winners
        return bracket

    def hard_cutoff_B(self, group) :
        bracket = self.bracket(group)
        tier = len(bracket)-1
        chosen = []
        while len(chosen) < self.pop_size/4 :
            for player in bracket[tier] :
                if len(chosen) >= self.pop_size/4 :
                    break
                chosen.append(player)
            tier -= 1
        return chosen

    def stochastic_B(self, group) :
        bracket = self.bracket(group)
        flat_bracket = [player for tier in range(len(bracket)-1, 0, -1) for player in bracket[tier]]
        chosen = []
        while len(chosen) < self.pop_size/4 :
            round = []
            while len(round) < self.pop_size/8 :
                player = rand.choice(flat_bracket)
                if player in round :
                    continue
                round.append(player)
            if len(flat_bracket) < self.pop_size/4 + self.pop_size/8 :
                print('ran')
                return False
            round.sort(reverse=True, key=(lambda x : flat_bracket.index(x)))
            chosen.append(round[0])
            flat_bracket.remove(round[0])
        return chosen

    def tournament_B(self, group) :
        grup = group.copy()
        chosen = []
        while len(chosen) < self.pop_size/4 :
            round = []
            while len(round) < self.pop_size/8 :
                player = rand.choice(grup)
                if player in round :
                    continue
                round.append(player)
            if len(grup) < self.pop_size/4 + self.pop_size/8 :
                return False
            bracket = self.bracket(round)
            chosen.append(bracket[len(bracket)-1][0])
            grup.remove(bracket[len(bracket)-1][0])
        return chosen

    def calc_avg_freq(self, group) :
        data = {'state_win': 0, 'win': 0, 'state_block': 0, 'block': 0}
        for state in self.good_moves :
            no_moves = True
            if self.good_moves[state]['win_moves'] != [] :
                data['state_win'] += 1
                no_moves = False
            if self.good_moves[state]['block_moves'] != [] :
                data['state_block'] += 1
                no_moves = False
            if no_moves :
                continue
            for strat in group :
                if strat[state] in self.good_moves[state]['win_moves'] :
                    data['win'] += 1
                if strat[state] in self.good_moves[state]['block_moves'] :
                    data['block'] += 1
        win_avg = data['win']/data['state_win']
        win_avg = win_avg/self.pop_size
        block_avg = data['block']/data['state_block']
        block_avg = block_avg/self.pop_size
        return [win_avg, block_avg]

    def for_generation(self, gen) :
        wanted_data = {0: {'vs_1': 0, 'vs_prev': 0, 'freq': self.calc_avg_freq(self.gen_0)}}
        prev_gen = self.gen_0
        cur_gen = []
        generation = 1
        while prev_gen != cur_gen or generation < gen :
            print(generation)
            #top = self.find_top(prev_gen, 5)      
            #top = self.tournament(prev_gen)
            top = self.stochastic(prev_gen)
            print(type(top), '\n')
            if top == False :
                return wanted_data  
            cur_gen = self.mate(top)
            cur_gen.extend(top)
            wanted_data[generation] = {'vs_1': self.avg_score(cur_gen, self.gen_0),
                                        'vs_prev': self.avg_score(cur_gen, prev_gen),
                                        'freq': self.calc_avg_freq(cur_gen)}
            
            prev_gen = cur_gen
            generation += 1
            #print('\n\n')
        return wanted_data

    def run_game(self, players) :
        index = 1
        winner = None
        board = ['0' for _ in range(9)]
        while winner == None :
            plr = players[index-1]
            choice = plr[''.join(board)]
            if choice != [] :
                board[choice] = str(index)

            winner = self.check_for_winner(board)
            index = (index % 2) + 1
        return winner

    def organize_board(self, board) :
        board = ''.join(board)

        thing = [board[index: index+3] for index in range(0,9,3)] #row
        for index in range(3) :
            thing.append(board[index] + board[index+3] + board[index+6]) #column
        thing.extend([board[0] + board[4] + board[8], board[2] + board[4] + board[6]]) #diagonal
        return thing

    def check_for_winner(self, board) :
        thing = self.organize_board(board)
        for stuff in thing :
            if len(set(stuff)) == 1 and '0' not in set(stuff) :
                return int(stuff[0])
        if '0' not in board :
            return 'tie'
                