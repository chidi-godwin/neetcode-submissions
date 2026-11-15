from collections import defaultdict


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(set)
        cols = defaultdict(set)
        squares = defaultdict(set)

        for r in range(9):
            for c in range(9):
                cell = board[r][c]
                sqr_idx = (r // 3, c // 3)

                if cell == '.':
                    continue

                if cell in rows[r] or cell in cols[c] or cell in squares[sqr_idx]:
                    return False
                rows[r].add(cell)
                cols[c].add(cell)
                squares[sqr_idx].add(cell)
        return True
