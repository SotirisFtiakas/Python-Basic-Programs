# Fibonacci number generator

# x: which x-th Fibonacci number we want to generate
def Fibonacci(x):
    if x==1:
        return 0
    elif x==2:
        return 1
    else:
        a,b=0,1
        for i in range (x-2):
            a,b = b, a + b
        return b

if __name__ == "__main__":
    print(Fibonacci(10))
