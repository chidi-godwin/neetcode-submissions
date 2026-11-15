class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row = len(board)
        column = len(board[0])

        is_valid = True

        # row validity check
        for i in range(row):
            seen = set()
            for j in range(column):
                cell = board[i][j]
                if cell == '.':
                    continue
                if cell in seen:
                    return False
                seen.add(cell)

        # column validity check
        for j in range(column):
            seen = set()
            for i in range(row):
                cell = board[i][j]
                if cell == '.':
                    continue
                if cell in seen:
                    return False
                seen.add(cell)

        # 3 sqaure validity check
        for square in range(9):
            seen = set()
            for i in range(9):

                row = 3 * (square // 3) + (i // 3)
                col = 3 * (square % 3) + (i % 3)

                cell = board[row][col]
                if cell == '.':
                    continue

                if cell in seen:
                    return False

                seen.add(cell)

        return True




            