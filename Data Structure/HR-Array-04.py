nd = input().split()

n = int(nd[0])

d = int(nd[1])
    
list = list(map(int, input().rstrip().split()))


shift = d

while True :
  temp = list.pop(0)  
  list.append(temp)
  shift -= 1
  if(shift == 0) :
    print(*(list))
    break