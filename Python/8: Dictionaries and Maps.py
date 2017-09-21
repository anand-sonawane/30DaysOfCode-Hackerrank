N=int(input())
dict_test = {}
str_name = ""
str_no = ""
for i in range(N):
    input_str = input().split()
    dict_test[input_str[0]] = input_str[1]
try:    
    while(1):
        input_str = input()
        if(input_str!=""):
            output_str = dict_test.get(input_str)
            if output_str is None:
                print("Not found")
            else:
                print(input_str + "=" +output_str)
        else:
            break
except EOFError:
    pass

