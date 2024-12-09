def fact(n):
    if(n == 0 or n == 1):
        return 1
    else: 
        return n * fact (n-1)

#----------Main Body-------------
answer = fact(4)
print(answer)