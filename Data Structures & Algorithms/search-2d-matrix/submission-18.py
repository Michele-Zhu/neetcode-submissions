class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # find closest in sorted array
        def find_row(arr, left, right, target):
            if left > right: 
                return right

            mid = left + (right - left) // 2
            #if arr[mid] == target:
            #    return mid

            if arr[mid] <= target:
                return find_row(arr, mid+1, right, target)
            else: # update best idx
                # self.idx = mid
                return find_row(arr, left, mid-1, target)

        def find_row2(arr, left, right, target):
            if left > right:
                return left
            mid = left + (right - left) // 2
            if arr[mid] == target:
                return mid
            if arr[mid] < target:
                return find_row2(arr, mid+1, right, target)
            else:
                return find_row2(arr, left, mid-1, target)

        def binary_search(arr, low, high, target):
            if low > high:
                return -1 # base case, target not found

            mid = low + (high - low) //2
            if arr[mid] == target:
                return mid
            elif arr[mid] > target: # search left
                return binary_search(arr, low, mid-1, target)
            else:
                return binary_search(arr, mid+1, high, target)

        n_cols = len(matrix[0][:])
        n_rows = len(matrix)
        col_arr = [row[0] for row in matrix]
        print(matrix[0][:])
        print(f"col_arr: {col_arr}, len = {len(col_arr)}, target = {target}")

        # find the row index
        self.row_idx = 0
        
        self.row_idx = find_row(col_arr, 0, len(col_arr)-1, target)
        print(self.row_idx)

        print(matrix[self.row_idx])
        col_idx = binary_search(matrix[self.row_idx], 0, n_cols-1, target)
        print(col_idx)
        if col_idx != -1: return True
        else: return False