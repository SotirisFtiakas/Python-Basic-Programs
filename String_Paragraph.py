def parag(x,length):
    newString = ""
    for i in range (len(x)):
        if i%length==0:
            newString+="\n"
        newString+=str(x[i])
    return newString



if __name__ == "__main__":
    input="Hello World What's Up!"
    length = 5
    
    print(parag(input,length))
