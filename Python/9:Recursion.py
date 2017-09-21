N=int(input())

def factorial(fact_n):
    if(fact_n==1):
        return 1
    else:
        return fact_n * factorial(fact_n-1)
ans = factorial(N)
print(ans)    
