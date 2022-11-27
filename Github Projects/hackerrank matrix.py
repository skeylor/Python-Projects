
array = [[1,2,3],
        [4,5,6],
        [7,8,9],
        [1,2,3],
        [4,5,6],
        [7,8,9]]
num = 0
hour_glass_sum = 0
for i in range(3):
    hour_glass_sum += array[num][i]
    hour_glass_sum += array[num+2][i]
print(hour_glass_sum)
        
        