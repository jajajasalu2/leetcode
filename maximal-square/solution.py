class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        if not matrix:
            return 0
        rows = len(matrix)
        cols = len(matrix[0])
        dp = [[0 for x in range(cols + 1)] for y in range(rows + 1)]
        maxsqlen = 0
        for i in range(1, rows + 1):
            for j in range(1, cols + 1):
                if matrix[i - 1][j - 1] == "1":
                    dp[i][j] = (
                        min(dp[i - 1][j], dp[i - 1][j - 1], dp[i][j - 1]) + 1
                    )
                    maxsqlen = max(maxsqlen, dp[i][j])
        return maxsqlen * maxsqlen
