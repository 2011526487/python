n=int(input('n:'))
def digui(n):
    if n==1:
        return 1
    return digui(n-1)*n
print(digui(n))