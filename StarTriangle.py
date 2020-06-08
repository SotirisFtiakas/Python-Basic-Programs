# Draw a Triangle made of stars *

# x: number of lines our triangle will have
def starT(x):
    for i in range (x):
        spaces= x-1-i

        print(spaces*" " + (i+(i+1))*"*" + spaces*" ")

if __name__ == "__main__":
    starT(9)