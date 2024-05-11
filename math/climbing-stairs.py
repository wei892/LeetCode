class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """

        arr = [0, 1, 2]
        for x in range(3, n+1):
            arr.append(arr[x-2] + arr[x-1])
        

        return arr[n]
'''
        countCombo = [0]

        def findCombo(n):
            if n == 0: 
                countCombo[0] += 1
                return
            
            if n >= 2:
                findCombo(n-2)
            if n >= 1:
                findCombo(n-1)
        
        findCombo(n)
        return countCombo[0]
'''