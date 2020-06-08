# map() function testing

def add(x):
    return x+2


if __name__ == "__main__":
    a = (1,2,3,5,8)
    res = map(add,a)
    print(list(res))