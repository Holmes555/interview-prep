class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        n = len(blocks)
        black = sum(1 for block in blocks[0:k] if block == 'B')
        min_col = k - black
        for i in range(1, n - k + 1):
            if blocks[i - 1] == 'B':
                black -= 1
            if blocks[i + k - 1] == 'B':
                black += 1
            min_col = min(min_col, k - black)
        return min_col
