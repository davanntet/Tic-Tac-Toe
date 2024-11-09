from copy import deepcopy

class AI:
    def __init__(self, players):
        self.name = 'AI'
        self.version = 1
        self.players = players
        self.state = None

    def __str__(self):
        return self.name + ' v' + str(self.version)

    def player(self, state):
        counts = {p: 0 for p in self.players}
        for row in state:
            for cell in row:
                if cell in self.players:
                    counts[cell] += 1
        return self.players[0] if counts[self.players[0]] <= counts[self.players[1]] else self.players[1]

    def actions(self, state):
        return [(i, j) for i, row in enumerate(state) for j, cell in enumerate(row) if cell is None]

    def result(self, state, action):
        new_state = deepcopy(state)
        row, col = action
        new_state[row][col] = self.player(state)
        return new_state

    def terminal(self, state):
        if not self.actions(state) or self.utility(state) != 0:
            return True, self.utility(state)
        return False, 0

    def utility(self, state):
        for i in range(3):
            if state[i][0] == state[i][1] == state[i][2] and state[i][0] is not None:
                return 1 if state[i][0] == self.players[0] else -1
            if state[0][i] == state[1][i] == state[2][i] and state[0][i] is not None:
                return 1 if state[0][i] == self.players[0] else -1
        if state[0][0] == state[1][1] == state[2][2] and state[0][0] is not None:
            return 1 if state[0][0] == self.players[0] else -1
        if state[0][2] == state[1][1] == state[2][0] and state[0][2] is not None:
            return 1 if state[0][2] == self.players[0] else -1
        return 0

    def minimax_decision(self, state):
        current_player = self.player(state)
        actions = self.actions(state)
        if current_player == self.players[0]:
            return self.max_value(state)
        else:
            return self.min_value(state)

    def max_value(self, state):
        game_checking = self.terminal(state)
        if game_checking[0]:
            return game_checking[1], None
        v = -float('inf')
        best_action = None
        for action in self.actions(state):
            # v = max(v, self.min_value(self.result(state, action)))
            if v<self.min_value(self.result(state, action))[0]:
                v = self.min_value(self.result(state, action))[0]
                best_action = action
        return v, best_action


    def min_value(self, state):
        game_checking = self.terminal(state)
        if game_checking[0]:
            return game_checking[1], None
        v = float('inf')
        best_action = None
        for action in self.actions(state):
            # v = min(v, self.max_value(self.result(state, action)))
            if v>self.max_value(self.result(state, action))[0]:
                v = self.max_value(self.result(state, action))[0]
                best_action = action
        return v, best_action
