# Primality test

def prime(x):
    if x%2==0:
        return False
    for i in range (3,x,2):
        if x%i==0:
            return False
    return True

if __name__ == "__main__":
    num = 1046527
    isPrime = prime(num)
    if isPrime:
        print("{} is Prime".format(num))
    else:
        print("{} is not Prime".format(num))
