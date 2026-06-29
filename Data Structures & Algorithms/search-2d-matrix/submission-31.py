class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        def find_row(left, right, target):
            if left > right:
                return left

            mid = left + (right - left) // 2
            if arr[mid] == target:
                return mid

            if arr[mid] > target: # go left
                return find_row(left, mid-1, target)
            elif arr[mid] < target and arr[mid+1] > target:
                return mid
            else: # right
                return find_row(mid+1, right, target)

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

        # find the row index
        col_arr = [row[0] for row in matrix]
        arr = col_arr
        row_idx = 0
        row_idx = find_row( 0, len(col_arr)-2, target)
        print(row_idx)

        # find the col index, -1 if not found
        col_idx = binary_search(matrix[row_idx], 0, n_cols-1, target)

        return col_idx != -1