#!/usr/bin/env python3

data = (
    [1, 5, 2, 3, 4],
    [4, 5, 0, 4]
)


def solve(list1, list2):
    '''Find common elements of two given lists.

    Returns a list contains those elements.
    Require: use only lists, and loop.
    '''
    result = []
    i=0
    for indexL1 in list1:
        for indexL2 in list2:
            if (indexL1 == indexL2) and (indexL2 not in result):
                result.append(indexL2)

#result = [element for element in list1 if element in list2] 
    
    return result


def main():
    L1, L2 = data
    print(solve(L1, L2))


if __name__ == "__main__":
    main()
