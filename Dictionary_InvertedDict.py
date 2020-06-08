# Create an inverted dictionary from the dictionary givev

def invDict(dict):
    inverted = {dict[i]: i for i in dict}
    return inverted


if __name__ == "__main__":
    ages = {
      "Sotos": 21,
      "Greg": 20,
      "John": 14,
    }

    print(invDict(ages))
