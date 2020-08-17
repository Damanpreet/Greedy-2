# count the number of tasks with maxfrequency (pair the maximum frequency tasks together)
# calculate the number of paritions that can be formed with the max freq tasks.
# calculate the empty spots based on it.
# calculate the number of idle spots that would be required. (empty-no of pending task).
# return the number of tasks + idle.
# Time complexity - O(n) # to calculate the maximum frequency task. -> actual - O(2n)
# Space complexity - O(1) # maximum would be 26 characters.
# Did this code run on leetcode? - yes

from collections import Counter
import operator
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        l = len(tasks)
        if l==0: return 0
        # iterate over the tasks and find the maximum frequency task.
        counts = Counter(tasks)
        # val = max(counts.items(), key=operator.itemgetter(1))
        
        # find the maximum frequency tasks.
        maxfreq = 0
        maxfreqvals = 0
        for _, count in counts.items():
            if count == maxfreq:
                maxfreqvals += 1
            elif count > maxfreq:
                maxfreqvals = 1
                maxfreq = count
        
        # no of partitions
        partitions = maxfreq-1
        
        # no of empty spots
        empty = (n-maxfreqvals+1) * partitions 
        
        # no of pending items
        pending = l - maxfreq*maxfreqvals
        
        # idle spots
        idle = max(0, empty-pending)
        
        return idle + l
    
    
# brute force method
# find the maximum frequency task at every step and add them to the scheduled tasks list.
# TLE
import copy
import numpy as np
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # count the number of tasks of each task type.
        counts_task = [0] * 27
        counts_task[26] = 1
        for task in tasks:
            task = ord(task)-65
            counts_task[task] += 1
        
        scheduled_tasks = []
        
        i,curridx=0,0
        while i<len(tasks):
            j=1
            ctasks = copy.deepcopy(counts_task)
            while j <= n and curridx-j>=0:
                prevtask = scheduled_tasks[curridx-j]
                if prevtask!=26: ctasks[prevtask]=0
                j+=1
            curridx+=1
            currtask = np.argmax(ctasks)
            scheduled_tasks.append(currtask)
            if currtask != 26: # if not dummy task
                i+=1
                counts_task[currtask]-=1
            # print(currtask, counts_task)
        
        return curridx
        