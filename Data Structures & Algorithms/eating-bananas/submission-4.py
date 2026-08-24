class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        '''
        If the pile has less than k, you can finish but then wait

        max is the number of piles
        min is 1
        rate is the k, bananas per hour
        upper for k is the end of the list. 
        '''
        l, r = 1, max(piles)
        minTime = max(piles)
        
        while l <= r:
            mid = (l + r) // 2
            hours = 0
            for i in piles:
                hours += math.ceil(i / mid)
            if hours > h:
                l = mid + 1
            elif hours <= h:
                if mid < minTime:
                    minTime = mid
                r = mid - 1
            
        return minTime
            




            






        
        