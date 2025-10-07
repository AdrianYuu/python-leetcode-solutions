class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        length = len(board)

        # left to right
        for i in range(length):
            occurrences = defaultdict(bool)

            for j in range(length):
                if board[i][j] == '.':
                    continue

                if occurrences[board[i][j]] == True:
                    print('1.', board[i][j])
                    return False

                occurrences[board[i][j]] = True

        # top to bottom
        for i in range(length):
            occurrences = defaultdict(bool)

            for j in range(length):
                if board[j][i] == '.':
                    continue

                if occurrences[board[j][i]] == True:
                    print('2.', board[j][i])
                    return False

                occurrences[board[j][i]] = True

        # center
        center_x = [1, 4, 7]
        center_y = [1, 4, 7]
        dir_x = [1, 1, -1, -1, 0, 0, 1, -1]
        dir_y = [1, -1, 1, -1, 1, -1, 0, 0]

        for x in center_x:
            for y in center_y:
                occurrences = defaultdict(bool)

                if board[x][y] != '.':
                    occurrences[board[x][y]] = True

                for i in range(8):
                    dx = dir_x[i]
                    dy = dir_y[i]
                    
                    if board[x + dx][y + dy] == '.':
                        continue

                    if occurrences[board[x + dx][y + dy]] == True:
                        return False

                    occurrences[board[x + dx][y + dy]] = True

        return True