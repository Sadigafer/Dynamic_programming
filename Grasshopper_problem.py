# Grasshopper Problem

count_of_cells = 10
count_of_variants = [0]*count_of_cells

for i in range(2,count_of_cells):
    count_of_variants[0] = 1
    count_of_variants[1] = 1
    count_of_variants[i] = count_of_variants[i-2] + count_of_variants[i-1]

print(count_of_variants) # [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]