class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        #traverses outer loop
        for i in range(len(matrix)):
            l, r = 0, len(matrix[i]) - 1
            while l <= r:
                mid = (l + r)//2
                if target > matrix[i][mid]:
                    l = mid + 1
                elif target < matrix[i][mid]:
                    r = mid - 1
                else:
                    return True
        return False
        

        
        