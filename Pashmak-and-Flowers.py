n = int(input())

my_list = []

my_list = list(map(int, input().split()))

my_list.sort()
c1 = my_list[0]
c2 = my_list[len(my_list)-1]

max_distance = c2 - c1
print(max_distance, end=" ")

if(max_distance == 0):
    print(int((n*(n-1))/2))
else:
    cnt1 = 0
    cnt2 = 0
    for i in range(len(my_list)):
        if(my_list[i] == c1):
            cnt1 += 1
        elif(my_list[i] == c2):
            cnt2 += 1

    print(cnt1 * cnt2)
