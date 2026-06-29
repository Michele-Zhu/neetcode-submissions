class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # Greedy algo, O(m) time, O(1) space, m the number of tasks
        # We think in terms of slots 
        # let maxf the max frequency of any task, i.e. A with 5 appeareances
        # We place A__A__A__A__A
        # there are maxf - 1 gaps between the most frequent tasks
        # each gap must be at least size n to satisfy the cooldonw
        # so initial idle slots needed = (maxf-1) * n
        # We can try to fill the idle slots using other tasks:
        # for each task with count c, it can fil up to min(c, maxf-1) of these gaps
        # subtract this filled amount from the idle slots
        # after considering all tasks if idle is still positive, we must add those idle slots to the total time
        # if idle becomes zero or negative it means all gaps are already filled (or over filled by tasks),
        # no need extra idle time
        # -> total time is len(tasks) (each task takes 1 unit ) + max(0, idle) (extra gaps we couldn't fill)

        # 1. Count task frequency
        # 2. find maxf = max frequency amoung all tasks
        # 3. compute idle slots: idle = (maxf - 1) * n
        # 4. For each task with count c:
        #       - Decrease idle by min(maxf - 1, c) (this task helps fill gaps)
        # 5. If idle is still positive, total time = len(tasks) + idle
        # 6. if idle is zero or negative, total time = len(tasks) (no extra idle needed)
        # 7. return total time

        count = [0] * 26 # frequency array
        for task in tasks:
            count[ord(task) - ord('A')] += 1
        
        count.sort()
        maxf = count[25]
        #print(maxf)
        #print(count)
        idle = (maxf-1) * n  # A__A__A__A
        for i in range(24, -1, -1):
            idle -= min(count[i], maxf-1)
        if idle>0:
            return len(tasks) + idle
        else:
            return len(tasks)