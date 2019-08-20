# Demonstrate built-in utility functions

def main():
    # use any() and all() to test sequences for boolean values
    l1 = [1,2,3,0,5,6]

    # TODO: any() will return True if any of the sequence values are True
    print(any(l1))

    # TODO: all() will return True if all of the sequence values are True
    print(all(l1))

    # TODO: min() and max() will return the minimum and maximum values in a sequence
    print("min: ",min(l1))
    print("max: ",max(l1))

    # TODO: use sum() to sum up all the values in a sequence
    print("sum: ",sum(l1))

main()