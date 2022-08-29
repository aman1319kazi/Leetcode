class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        m, n = len(mat), len(mat[0])
        di = defaultdict(list)
        
        for x in range(m):
            for y in range(n):
                di[x - y].append(mat[x][y])
                
        for key, val in di.items():
            val.sort(reverse = True)
            
        for x in range(m):
            for y in range(n):
                mat[x][y] = di[x - y].pop()
        return mat