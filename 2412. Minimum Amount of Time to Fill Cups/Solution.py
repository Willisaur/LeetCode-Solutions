class Solution:
    def fillCups(self, amount: List[int]) -> int:
        # make a max heap
        amount = [-x for x in amount]
        heapq.heapify(amount)

        # make time variable
        second = 0

        # fill cups
        while amount[0] != 0:
            print(amount)
            # remember to use negative numbers since max heap
            temp = amount[0]
            heapq.heappop(amount)
            heapq.heappush(amount, temp+1) 

            if amount[0] == temp:
                heapq.heappop(amount)
                heapq.heappush(amount, temp+1)
            elif amount[1] < 0:
                temp = heapq.heappop(amount)
                temp2 = heapq.heappop(amount)
                heapq.heappush(amount, temp)
                heapq.heappush(amount, temp2+1)
            
            second += 1
        
        return second
