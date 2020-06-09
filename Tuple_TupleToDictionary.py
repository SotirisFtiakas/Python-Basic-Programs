# Make a tuple into a dictionary

def tupleToDict(x):
    myDict={}
    for i in x:
        myDict[i[0]]=i[1]
    return myDict


if __name__ == "__main__":
    input = ((2, "w"),(3, "r"))
    print(tupleToDict(input))