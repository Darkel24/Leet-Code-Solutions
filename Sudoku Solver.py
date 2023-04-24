class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        def getBit(x, k): return (x >> k) & 1
        def setBit(x, k): return (1 << k) | x
        def clearBit(x, k): return ~(1 << k) & x

        rows, cols, boxes = [0] * 9, [0] * 9, [0] * 9
        emptyCells = []
        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    emptyCells.append([r, c])
                else:
                    val = int(board[r][c])
                    boxPos = (r // 3) * 3 + (c // 3)
                    rows[r] = setBit(rows[r], val)
                    cols[c] = setBit(cols[c], val)
                    boxes[boxPos] = setBit(boxes[boxPos], val)

        def backtracking(i):
            if i == len(emptyCells): return True  # Check if we filled all empty cells?

            r, c = emptyCells[i]
            boxPos = (r // 3) * 3 + c // 3
            for val in range(1, 10):
                if getBit(rows[r], val) or getBit(cols[c], val) or getBit(boxes[boxPos], val): continue  # skip if that value is existed!
                board[r][c] = str(val)
                rows[r] = setBit(rows[r], val)
                cols[c] = setBit(cols[c], val)
                boxes[boxPos] = setBit(boxes[boxPos], val)
                if backtracking(i + 1): return True
                rows[r] = clearBit(rows[r], val)
                cols[c] = clearBit(cols[c], val)
                boxes[boxPos] = clearBit(boxes[boxPos], val)
            return False

        backtracking(0)
