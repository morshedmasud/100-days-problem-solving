input = [
        [1,1,1,0,0,0],
        [0,1,0,0,0,0],
        [1,1,1,0,0,0],
        [0,9,2,-4,-4,0],
        [0,0,0,-2,0,0],
        [0,0,-1,-2,-4,0]
        ]

# input = [[1,1,1,0,0,0],
# [0,1,0,0,0,0],
# [1,1,1,0,0,0],
# [0,0,2,4,4,0],
# [0,0,0,2,0,0],
# [0,0,1,2,4,0]]

sum_list = []


def sum_list_s(list):
  sum = 0
  for i in list:
    sum += i
    
  return sum


for i in range(4):

    sum = input[i][0]+ input[i][1]+input[i][2] + input[i+1][1] + input[i+2][0]+ input[i+2][1]+input[i+2][2] 
    sum_list.append(sum)
    
    sum = input[i][1]+ input[i][2]+input[i][3] + input[i+1][2] + input[i+2][1]+ input[i+2][2]+input[i+2][3] 
    sum_list.append(sum)
    
    sum = input[i][2]+ input[i][3]+input[i][4] + input[i+1][3] + input[i+2][2]+ input[i+2][3]+input[i+2][4] 
    sum_list.append(sum)
    
    sum = input[i][3]+ input[i][4]+input[i][5] + input[i+1][4] + input[i+2][3]+ input[i+2][4]+input[i+2][5] 
    sum_list.append(sum)

#     sum = sum_list_s(input[i][0:3]) + input[i+1][1]+ sum_list_s(input[i+2][0:3]) 
#     sum_list.append(sum)
    
#     sum = input[i][1]+ input[i][2]+input[i][3] + input[i+1][2] + input[i+2][1]+ input[i+2][2]+input[i+2][3] 
#     sum_list.append(sum)
    
#     sum = input[i][2]+ input[i][3]+input[i][4] + input[i+1][3] + input[i+2][2]+ input[i+2][3]+input[i+2][4] 
#     sum_list.append(sum)
    
#     sum = input[i][3]+ input[i][4]+input[i][5] + input[i+1][4] + input[i+2][3]+ input[i+2][4]+input[i+2][5] 
#     sum_list.append(sum)

print((sum_list))
  

    
        
    
    