class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        directions = list(product([0, 1, -1], [0, 1, -1]))
        directions.pop(directions.index((0, 0)))
        for i, l in enumerate(board):
            for j, e in enumerate(l):
                ref = 0
                for di, dj in directions:
                    if 0 <= i + di < len(board) and 0 <= j + dj < len(board[0]):
                        ref += board[i + di][j + dj]
                ref &= 0xf
                if ref == 3:
                    board[i][j] |= 1 << 4
                elif ref == 2 and e == 1:
                    board[i][j] |= 1 << 4
                else:
                    board[i][j] &= 0xf
        for i, l in enumerate(board):
            for j, e in enumerate(l):
                board[i][j] >>= 4