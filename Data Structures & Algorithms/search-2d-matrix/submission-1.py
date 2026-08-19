class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        #Determine which row to choose
        top, below = 0, len(matrix) - 1
        midR = 0
        while top <= below:
            midR = (top + below) // 2
            if target < matrix[midR][0]:
                below = midR - 1
            elif target > matrix[midR][-1]:
                top = midR + 1
            else:
                break
                
        
        l, r = 0, len(matrix[midR]) - 1
        while l <= r:
            mid = (l + r)//2
            if target > matrix[midR][mid]:
                l = mid + 1
            elif target < matrix[midR][mid]:
                r = mid - 1
            else:
                return True
        return False

            

        #Binary search within that row
        

        
        