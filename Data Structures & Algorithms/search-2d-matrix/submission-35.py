class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        def binary_search(left, right):
            if left > right:
                return False

            mid = left + (right - left) // 2
            row = mid // n_cols
            col = mid % n_cols
            #print(f"bin_search element ({row, col}), value {matrix[row][col]}")
            
            if matrix[row][col] == target:
                return True
            elif matrix[row][col] > target: # search left subarray
                return binary_search(left, mid-1)
            else: # search right subarray
                return binary_search(mid+1, right)
        
        n_cols = len(matrix[0][:])
        n_rows = len(matrix)
        #print(n_rows, n_cols, n_rows*n_cols-1)
        return binary_search(0, n_rows*n_cols -1)