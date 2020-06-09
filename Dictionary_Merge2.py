# Write a Python script to merge two different Python dictionaries.

def mergeDicts(d1, d2):
    d3 = d1.copy()
    d3.update(d2)
    return d3

if __name__ == "__main__":
    d1 = {'a': 100, 'b': 200, 'c':'Hi'}
    d2 = {'x': 300, 'y': 200}
    newDict = mergeDicts(d1,d2)
    print(newDict)
