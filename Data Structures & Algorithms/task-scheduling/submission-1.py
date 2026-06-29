class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # create a max_heap that contains the tuple
        # (count, task_id, last)
        # we build a frequency array

        # THE OVERAL COMPLEXITY IS:
        # O(m) where m is the number of tasks, O(1) space since bounded number of tasks

        # if I use hashmap is more general, O(T), where T is len(tasks), space O(T'),
        # T' number of distinct tasks
        counts = {}
        for task in tasks:  # O(T), O(T)
            if task in counts.keys():
                counts[task] += 1
            else:
                counts[task] = 1
        # print(counts)

        max_heap = []
        heapq.heapify_max(max_heap)
        for task_id, count in counts.items(): # O(T log k), O(log k)
            heapq.heappush_max(max_heap, [count, task_id])  # O(log )
        # print(max_heap)

        queue = deque()
        t = 0
        while max_heap or queue:  # O(log k), (time * log k)
            t += 1
            if max_heap:  # tasks to schedule
                count, task_id = heapq.heappop_max(max_heap)
                if count - 1 > 0:
                    next_available_time = t + n
                    queue.append([count - 1, task_id, next_available_time])
            else:  # no schedulable tasks, but some in wait
                t = queue[0][2]
            while queue and queue[0][2] == t:
                count, task_id, next_avail_t = queue.popleft()
                heapq.heappush_max(max_heap, [count, task_id])
            # print(f"time t={t} end loop we have: {max_heap}, {queue}")
        return t