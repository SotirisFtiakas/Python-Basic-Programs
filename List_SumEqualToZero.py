# Write a Python program to find three numbers from an array such that the sum of three numbers equal to zero.
# Find the unique triplets in the array.

def sumZero(x):
    length = len(x)-1
    myList=[]
    for i in range(length):
        for j in range(i+1,length):
            for k in range(j+1,length):
                if (x[i]+x[j]+x[k])==0:
                    sortedL = [x[i],x[j],x[k]]
                    sortedL.sort()
                    if sortedL not in myList:
                        myList.append(sortedL)

    for i in myList:
        print(i)


if __name__ == "__main__":

    input = [-1, 0, 1, 2, -1, -4]
    sumZero(input)