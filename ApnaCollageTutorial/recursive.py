# Write a recursive function to calculate the sum of first n natural numbers

def calc_Sum(n):
    if (n == 0):
        return 0
    else:
        return calc_Sum(n-1) + n

sum = calc_Sum(10)
print(sum)