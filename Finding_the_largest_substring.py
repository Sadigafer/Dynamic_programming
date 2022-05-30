# Finding the largest substring

word_1 = ["М","О","Л","О","К","О"]
word_2 = ["О","К","О","Л","О"]

matrix = [[0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0]]

for i in range (1,len(matrix)):
     for j in range (1,len(matrix[0])):
        if word_1[j-1] == word_2[i-1]:
            matrix[i][j] += 1 + matrix[i-1][j-1]
        else:
            matrix[i][j] = max(matrix[i-1][j],matrix[i][j-1])
print(matrix)
'''
[[0, 0, 0, 0, 0, 0, 0],
[0, 0, 1, 1, 1, 1, 1],
[0, 0, 1, 1, 1, 2, 2],
[0, 0, 1, 1, 2, 2, 3],
[0, 0, 1, 2, 2, 2, 3],
[0, 0, 1, 2, 3, 3, 3]]
'''