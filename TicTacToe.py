class TicTacToeBoard:
    def __init__(self):
        self.new_game()

    def new_game(self):
        self.board = [[2, 2, 2]] * 3
        self.result = None
        self.turn = 1

    def get_board(self):
        output = []
        for i in self.board:
            x = []
            for j in i:
                if j == 2:
                    x.append('-')
                elif j == 1:
                    x.append('X')
                else:
                    x.append('0')
            output.append(x)
        return output

    def check_field(self):
        if self.board[0][0]+self.board[1][1]+self.board[2][2] == 3 or \
            self.board[0][2]+self.board[1][1]+self.board[2][0] == 3 or \
            self.board[0][0] + self.board[0][1] + self.board[0][2] == 3 or \
            self.board[1][0] + self.board[1][1] + self.board[1][2] == 3 or \
            self.board[2][0] + self.board[2][1] + self.board[2][2] == 3 or \
            self.board[0][0] + self.board[1][0] + self.board[2][0] == 3 or \
            self.board[0][1] + self.board[1][1] + self.board[2][1] == 3 or \
                self.board[0][2] + self.board[1][2] + self.board[2][2] == 3:
            self.result = 'X'
        elif self.board[0][0]+self.board[1][1]+self.board[2][2] == -3 or \
            self.board[0][2]+self.board[1][1]+self.board[2][0] == -3 or \
            self.board[0][0] + self.board[0][1] + self.board[0][2] == -3 or \
            self.board[1][0] + self.board[1][1] + self.board[1][2] == -3 or \
            self.board[2][0] + self.board[2][1] + self.board[2][2] == -3 or \
            self.board[0][0] + self.board[1][0] + self.board[2][0] == -3 or \
            self.board[0][1] + self.board[1][1] + self.board[2][1] == -3 or \
                self.board[0][2] + self.board[1][2] + self.board[2][2] == -3:
            self.result = '0'
        elif sum(self.board[0])+sum(self.board[1])+sum(self.board[2]) == 1:
            self.result = 'D'
        return self.result

    def make_move(self, row, col):
        if self.result != None:
            return 'Игра уже завершена'
        if self.board[row-1][col-1] == 2:
            return f'Клетка {row}, {col} уже занята'
        self.board[row-1][col-1] = self.turn
        self.turn = -self.turn
        self.check_field()
        if self.result == 'D':
            return 'Ничья'
        if self.result == None:
            return 'Продолжаем играть'
        return f'Победил игрок {self.result}'
