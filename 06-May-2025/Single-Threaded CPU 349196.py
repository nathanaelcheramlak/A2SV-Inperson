# Problem: Single-Threaded CPU - https://leetcode.com/problems/single-threaded-cpu/

class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        for i in range(len(tasks)):
            tasks[i].append(i)

        tasks.sort()
        
        result = []
        min_heap = []
        time = 0
        task_idx = 0
        n = len(tasks)
        
        while len(result) < n:
            while task_idx < n and tasks[task_idx][0] <= time:
                enqueue_time, processing_time, index = tasks[task_idx]
                heappush(min_heap, (processing_time, index))
                task_idx += 1
            
            if min_heap:
                processing_time, index = heappop(min_heap)
                time += processing_time
                result.append(index)
            else:
                time = tasks[task_idx][0]

        return result

