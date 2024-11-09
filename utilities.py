
class Utilities:
    def generate_board(self, n_row, n_col):
        board = []
        for i in range(n_row):
            row = []
            for j in range(n_col):
                row.append(None)
            board.append(row)
        return board

    def who_winner(self, state):
        for i in range(3):
            if state[i][0] == state[i][1] == state[i][2] and state[i][0] is not None:
                return state[i][0]
            if state[0][i] == state[1][i] == state[2][i] and state[0][i] is not None:
                return state[0][i]
        if state[0][0] == state[1][1] == state[2][2] and state[0][0] is not None:
            return state[0][0]
        if state[0][2] == state[1][1] == state[2][0] and state[0][2] is not None:
            return state[0][2]
        return None