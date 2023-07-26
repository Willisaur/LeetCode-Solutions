class Solution:
    def isHappy(self, n: int) -> bool:
        # store the current number in a variable (n)
        # add this number to a hashmap to track if a cycle is occurring (better than a list; duplicate keys means cycle)
        # divide the number by 10 repetitively to get each digit
        # square each digit and add to get to the new number
        # if a cycle occurs, return False, otherwise return True
        
        val = 0
        cycle = dict()

        while n != 1:
            print(n)
            if n in cycle.keys():
                return False
            
            cycle[n] = 1
            
            while n > 0:
                val += (n % 10)**2
                n //= 10
            
            n = val
            val = 0

        return True
