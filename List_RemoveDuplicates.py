# Given a sentence containing n words/strings. Remove all duplicates words/strings which are similar to each others.

def remDup(x):
    myWords = x.split(" ")
    noDup=[]
    for i in myWords:
        if i not in noDup:
            noDup.append(i)
    output = ""
    for i in noDup:
        output+=i + " "
    return output


if __name__ == "__main__":
    input = "Python is so great and Java is also so great"
    print(remDup(input))