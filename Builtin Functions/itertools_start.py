import itertools

def testFunction(x):
    pass


def main():
    # TODO: cycle iterator can be used to cycle over a collection
    seq1 = ["Joe", "John", "Mike"]
    # cycle1 = itertools.cycle(seq1)
    # print(next(cycle1))
    # print(next(cycle1))
    # print(next(cycle1))
    # print(next(cycle1))

    # TODO: use count to create simple counter
    # count1 = itertools.count(100, 10)
    # print(next(count1))
    # print(next(count1))
    # print(next(count1))

    # TODO: accumulate creates an iterator that accumulates values
    vals = [10,20,30,40,50,40,30]
    # acc = itertools.accumulate(vals)
    acc = itertools.accumulate(vals, max)
    print(list(acc))


if __name__ == "__main__":
    main()