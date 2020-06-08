def revCap(x):
    newString = ""
    for i in x:
        if i.isupper():
            newString += i.lower()
        else:
            newString += i.upper()

    return newString


if __name__ == "__main__":
    word="Hello WorlD"
    print(revCap(word))
