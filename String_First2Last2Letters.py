# Return a new string consisting of the first 2 and last 2 letters of the string given
# If its length is <2 then return the empty string

def fl2(x):
    if len(x)<2:
        return ""

    return x[0:2] + x[-2:]

if __name__ == "__main__":
    word = "w223d"
    print(fl2(word))