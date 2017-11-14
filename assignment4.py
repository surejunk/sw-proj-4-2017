import time
import random
def factorial(n):
    if n==1 or n ==0:
        return 1
    else:
        return n*factorial(n-1)
if __name__ == '__main__':
    while 1:
        n=int(input("Enter a number:"))
        sum=0
        if n==-1:
            break
        print(n,"!=",factorial(n))
        ts=time.time()


