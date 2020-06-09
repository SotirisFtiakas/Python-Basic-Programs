# Find set differences and common elements

def setDiff(x,y):
    setz = setx.difference(sety)
    return setz

def setComm(x,y):
    setz = setx & sety
    return setz

if __name__ == "__main__":
    setx = set(["apple", "mango"])
    sety = set(["mango", "orange"])

    print(setDiff(setx,sety))
    print(setComm(setx,sety))