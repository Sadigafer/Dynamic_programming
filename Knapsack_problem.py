# Knapsack problem

matrix = [[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]]
cost = [1500,3000,2000]
weight = [1,4,3]

for i in range (1,len(matrix)):
    for j in range (1,len(matrix[0])):
        if j>=weight[i-1]:
            matrix[i][j] = max(matrix[i-1][j], cost[i-1]+matrix[i-1][j-weight[i-1]])
        else:
            matrix[i][j] = matrix[i-1][j]

print(matrix)
'''
[[0, 0, 0, 0, 0], 
[0, 1500, 1500, 1500, 1500], 
[0, 1500, 1500, 1500, 3000], 
[0, 1500, 1500, 2000, 3500]]
'''