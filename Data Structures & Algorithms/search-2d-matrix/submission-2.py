class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        topRow = 0
        botRow = len(matrix) - 1

        while topRow <= botRow:
            mid = topRow + (botRow - topRow) // 2
            if matrix[mid][0] > target:
                botRow = botRow - 1
            elif matrix[mid][-1] < target:
                topRow = topRow + 1
            else:
                break
        midRow = mid
        
        colLeft = 0
        colRight = len(matrix[0]) - 1
        while colLeft <= colRight:
            mid = colLeft + (colRight - colLeft)//2
            if matrix[midRow][mid] == target:
                return True
            elif matrix[midRow][mid] < target:
                colLeft = mid + 1
            else:
                colRight = mid - 1
        return False