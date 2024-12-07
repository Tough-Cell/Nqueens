import webbrowser

class Solution:
    # Class used on leetcode
    def solveNQueens(self, n: int) -> List[List[str]]:
        def backtrack(row):
            if row == n:
                result.append([''.join(board[i]) for i in range(n)])
                return
            
            for col in range(n):
                if col in cols or (row - col) in diag1 or (row + col) in diag2:
                    continue
                
                board[row][col] = 'Q'
                cols.add(col)
                diag1.add(row - col)
                diag2.add(row + col)
                
                backtrack(row + 1)
                
                board[row][col] = '.'
                cols.remove(col)
                diag1.remove(row - col)
                diag2.remove(row + col)
        
        result = []
        board = [['.'] * n for _ in range(n)]
        cols = set()
        diag1 = set()
        diag2 = set()
        
        backtrack(0)
        return result

if __name__ == "__main__":
	webbrowser.opennew("https://leetcode.cn/problems/n-queens/?envType=study-plan-v2&envId=top-100-liked")