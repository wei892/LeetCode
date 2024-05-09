class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        if len(piles) == h:
            return max(piles)
        
        minBanana = 1
        maxBanana = max(piles)
        result = maxBanana

        while minBanana <= maxBanana:
            mid = int((maxBanana + minBanana) / 2)

            hoursTook = 0
            for banana in piles:
                hoursTook += math.ceil(banana/mid)
            
            if hoursTook > h:
                minBanana = mid + 1
            elif hoursTook <= h:
                result = min(result, mid)
                maxBanana = mid - 1
        
        return result
            
        
        
        
        