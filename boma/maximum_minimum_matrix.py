# a) Algorithm:
# 	0.	Initialize an empty list called "result".
# 	0.	For each row "i" in the matrix, find the maximum value in the row and its column index.
# 	0.	Check if the maximum value is also the minimum value in its column. If it is, append the value to the "result" list.
# 	0.	Return the "result" list.
# b) Time complexity:
# 	•	We need to iterate over each row and each column once. Therefore, the time complexity of the algorithm is O(m*n).
# 	•	Finding the maximum value in a row and its column index takes O(n) time. The total time complexity of this step is O(m*n).
# Therefore, the overall time complexity of the algorithm is O(m*n).
# Space complexity:
# 	•	We only need to store the "result" list, which can contain at most one element. Therefore, the space complexity is O(1).
# c) Tests:
# Input: [[5,16,20],[9,11,18],[15,16,17]]
# Output: [17]
# Input: [[100,60,20,50],[70,80,10,90],[10,50,44,30]]
# Output: [50]
# To validate the answer, we can compare the output of the algorithm with the expected output for the given inputs.




Can you write the code in python?


Sure! Here's the Python code:
scss


Copy code
matrix = [[5,16,20],[9,11,18],[15,16,17]]
print(max_in_row_min_in_col(matrix)) # Output: [17] matrix = [[100,60,20,50],[70,80,10,90],[10,50,44,30]] print(max_in_row_min_in_col(matrix)) # Output: [50]

matrix = [[5,16,20],[9,11,18],[15,16,17]]
print(max_in_row_min_in_col(matrix))  # Output: [17]

matrix = [[100,60,20,50],[70,80,10,90],[10,50,44,30]]
print(max_in_row_min_in_col(matrix))  # Output: [50]

def max_in_row_min_in_col(matrix):
    result = []
    for i in range(len(matrix)):
        row_max = max(matrix[i])
        col_index = matrix[i].index(row_max)
        col_min = min(matrix[j][col_index] for j in range(len(matrix)))
        if row_max == col_min:
            result.append(row_max)
    return result
