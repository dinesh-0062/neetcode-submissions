class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]

        for row in range(9):
            for col in range(9):
                value = board[row][col]
                if value == ".":
                    continue

                box_index = (row // 3) * 3 + (col // 3)

                if value in rows[row] or value in cols[col]:
                    return False
                if value in boxes[box_index]:
                    return False

                rows[row].add(value)
                cols[col].add(value)
                boxes[box_index].add(value)

        return True


# Time Complexity: O(1), because the board is always 9 x 9.
# Space Complexity: O(1), because the sets hold at most 81 values.
