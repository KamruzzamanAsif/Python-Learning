t = int(input())

for i in range(t):
    n = int(input())
    my_list = list(map(int, input().split()))
    
    if(n%2 != 0):
        print("Mike")
        continue
    
    x = min(my_list)
    index = my_list.index(x)
    
    if((index+1)%2 != 0):
        print("Joe")
    else:
        print("Mike")
        
