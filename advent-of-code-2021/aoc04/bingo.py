def get_bingo_score(numbers_to_draw, boards_string):
    winning_board = None
    boards = get_boards_from_string(boards_string)
    for number in numbers_to_draw:
        for board in boards:
            board.check_number(number)
            if board.has_won():
                winning_board = board
                break
        if winning_board:
            break

    return winning_board.calculate_score()


def get_boards_from_string(boards_string):
    all_boards = []
    the_board = []
    row = 0
    for line in iter(boards_string.splitlines()):
        if line == "":
            continue
        the_board.append([int(item) for item in line.split(" ") if item != ""])
        row += 1
        if row == 5:
            row = 0
            the_board = []
            all_boards.append(Board(the_board))
    return all_boards


class Board:
    def __init__(self, numbers):
        self.board = numbers
        self.checked_numbers = []

    def check_number(self, number):
        for row in self.board:
            if number in row:
                self.checked_numbers.append(number)
                break

    def has_won(self):
        row_points = 0
        for row in self.board:
            for col in row:
                if col in self.checked_numbers:
                    row_points += 1
                if row_points == 5:
                    return True
            row_points = 0

        col_points = 0
        for i in range(0, 5):
            for row in self.board:
                if row[i] in self.checked_numbers:
                    col_points += 1
                if col_points == 5:
                    return True
            col_points = 0
        return False

    def calculate_score(self):
        points = 0
        for row in self.board:
            for col in row:
                if col not in self.checked_numbers:
                    points += col
        return points * self.checked_numbers[len(self.checked_numbers) - 1]
