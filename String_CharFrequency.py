# A program to count the number of characters (character frequency) in a string.

def freq(w):
    dict={}
    for i in w:
        if i not in dict:
            dict[i]=1
        dict[i]=dict[i]+1
    return dict


if __name__ == "__main__":
    word="google.com"
    print(freq(word))