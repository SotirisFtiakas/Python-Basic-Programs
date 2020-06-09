# Remove empty tuples from a given list of tuples.

def emptyTuples(x):
    y = [i for i in x if i!=()]
    return y

if __name__ == "__main__":

    input = [(), ('ram','15','8'), (), ('laxman', 'sita'),
                  ('krishna', 'akbar', '45'), ('',''),()]
    print(emptyTuples(input))