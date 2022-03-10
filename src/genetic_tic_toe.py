import random
#and tic-tac-toe...
class GeneticAlgorithm () :
    def __init__(self, num_players) :
        self.players = self.create_players(num_players)

    def get_possible_moves(self, game_state) :
        possible_moves = []
        for index in range(len(game_state)) :
            if game_state[index] == '0':
                possible_moves.append(index)
        if possible_moves == [] :
            possible_moves.append([])
        return possible_moves

    def create_players(self, num_players) :
        players = [{} for _ in range(num_players)]
        prev_choices = ['000000000']
        num = 1
        while prev_choices != [] :
            choice = prev_choices[0]
            possible_choices = self.get_possible_moves(choice)
            for player in players :
                player[choice] = random.choice(possible_choices)
            update = [choice[:value] + str(num) + choice[value+1:] for value in possible_choices]
            prev_choices.remove(choice)
            prev_choices.extend(update)
            num = (num % 2) + 1
        return players

    def find_player_scores(self, group_1, group_2) :
        plr_score = [{index : 0 for index in range(25)} for _ in range(2)]
        for plr_1 in range(25) :
            for plr_2 in range(25) :
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
        for plr_1 in range(25) :
            for plr_2 in range(25) :
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
    
    def find_top_5(self) :
        scores = self.find_plr_scores_same(self.players)
        scores = [score for score in scores.items()]
        scores.sort((lambda x : x[1]))
        return scores

class TicTacToe:
    def __init__(self, players) :
        self.players = players
        self.board = ['0' for _ in range(9)]
        self.winner = None
        self.run_game()

    def swap_plrs(self) :
        self.board = ['0' for _ in range(9)]

    def run_game(self) :
        index = 1
        while self.winner == None :
            plr = self.players[index]
            choice = plr[''.join(self.board)]
            if choice != [] :
                self.board[choice] = str(index)

            self.winner = self.check_for_winner()
            index = (index % 2) + 1

    def check_for_winner(self) :
        board = ''.join(self.board)

        thing = [board[index: index+3] for index in range(0,9,3)] #row
        for index in range(3) :
            thing.append([board[index] + board[index+3] + board[index+6]]) #column
        thing.extend([[board[0] + board[4] + board[8]], [board[2] + board[4] + board[6]]]) #diagonal

        for stuff in thing :
            if len(set(stuff)) == 1 and set(stuff) != {'0'} :
                return int(stuff[0])
        if '0' not in self.board :
            return 'tie'
                
    def print_board(self):
        for i in range(len(self.board)):
            row = self.board[i]
            row_string = ''
            for space in row:
                if space == None:
                    row_string += '_|'
                else:
                    row_string += space + '|'
            print(row_string[:-1])
        print('\n')