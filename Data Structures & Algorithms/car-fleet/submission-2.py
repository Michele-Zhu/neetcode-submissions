class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # time taken can be calculated as (float) (target - pos)/speed
        # Under which condition two cars collide? comparing time taken
        # this problem also need sorting the car based on it's position
        # usage of the stack fro time comparison

        # target - pos = distance to travel
        # time = (float) (target - pos)/speed
        time = [(float) (target-position[i])/speed[i] for i in range(len(position))]  # O(n)

        tuples = list(zip(position, speed, time))  # zip creation is O(1), convertion to list O(n)
        tuples = sorted(tuples, key=lambda x: x[0], reverse=True)  # Sorting is O(nlogn) -> timsort algorithm
        print(tuples)

        stacks = []
        for tuple in tuples:
            if len(stacks) == 0:
                stack = deque()
                stack.append(tuple)
                stacks.append(stack)
                continue
            
            current_time = tuple[2]
            # The car behind joins the fleet if its time is less than or EQUAL to the LEAD car of the fleet
            last_time = stacks[-1][0][2]  # check the lead car's time
            if current_time > last_time:  # car is in another fleet
                stack = deque()
                stack.append(tuple)
                stacks.append(stack)
            else: # car in the same fleet
                stacks[-1].append(tuple)


        return len(stacks)