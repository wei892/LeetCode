class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # totalCost = 0

        for x in range(2, len(cost)):
            cost[x] += min(cost[x-1], cost[x-2])
        
        return min(cost[len(cost)-1], cost[len(cost)-2])

        
        # step = 0
        # while step < len(cost)-1:
        #     if (cost[step + 1] < cost[step + 2]):
        #         step += 1
        #         totalCost += cost[step]
        #     else:
        #         step += 2
        #         totalCost += cost[step]
        
        # return totalCost
