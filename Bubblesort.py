# Bubblesort

# a: list of elements

def bs(a):
    b=len(a)-1

    for x in range (b-1):
        for y in range (x,b):
            if a[x]>a[y]:
                temp = a[x]
                a[x] = a[y]
                a[y] = temp

    return a

if __name__ == "__main__":
    a = [32, 5, 3, 6, 7, 54, 87]
    print(bs(a))