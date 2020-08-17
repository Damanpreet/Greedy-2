# begin by assigning one candy to every child.
# put the index of the minimum rating in a queue.
# begin by traversing the queue.
# check the rating of neighbors.
# Add neighbors to the queue if their rating is greater than the current index and the number of candies is less than the candies assigned to the current child.
# time complexity - O(n^2) -- worst case ??
# space complexity - O(2n) -- queue and candies array
# did this solution run on leetcode ? - no
from collections import deque

class Solution:
    def candy(self, ratings: List[int]) -> int:
        n = len(ratings) # number of children
        candies = [1] * n
        
        queue = deque(list(range(n)))
        while queue:
        
            top = queue.popleft()
            if (top+1) < n:
                if ratings[top+1] > ratings[top] and candies[top+1] <= candies[top]: 
                    candies[top+1] = candies[top] + 1 
                    queue.append(top+1)
                elif ratings[top+1] == ratings[top] and candies[top+1] < candies[top]:
                    # candies[top+1] = candies[top]
                    queue.append(top+1)
                
            if (top-1) >= 0:
                if ratings[top-1] > ratings[top] and candies[top-1] <= candies[top]: 
                    candies[top-1] = candies[top] + 1
                    queue.append(top-1)
                elif ratings[top-1] == ratings[top] and candies[top-1] < candies[top]:
                    # candies[top-1] = candies[top]
                    queue.append(top-1)
        
        return sum(candies)
            
    
# Time complexity - O(n)
# Space complexity - O(n)
# did this solution run on leetcode? - yes
class Solution:
    def candy(self, ratings: List[int]) -> int:
        n = len(ratings) # number of children
        candies = [1] * n
        
        # traverse to the right, and see if the right neighbor rating is greater than the current rating.
        for i in range(n-1):
            if ratings[i+1] > ratings[i]:
                candies[i+1] = candies[i]+1
                
        # traverse to the left, and see if the left neighbor rating is greater than the current rating.
        for i in range(n-1, 0, -1):
            if ratings[i-1] > ratings[i]:
                candies[i-1] = max(candies[i-1], candies[i]+1)
        
        return sum(candies)
        