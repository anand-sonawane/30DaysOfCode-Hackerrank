n=int(input())
for i in range(n):
    str_data = str(input())
    index = 0
    str_even=""
    str_odd=""
    for j in str_data:
        if(index%2==0):
            str_even+=j
        else:
            str_odd+=j
        index+=1
    print(str_even + " " + str_odd)
