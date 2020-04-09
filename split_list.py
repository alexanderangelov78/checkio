def split_list(items: list) -> list:
    # your code here
    if len(items) == 0:
        return [[],[]]
    elif len(items) == 1:
        return [items,[]]
    elif len(items) % 2 == 0:
        l1 = []
        l2 = []
        for i in range(0, int(len(items) // 2)):
            l1.append(items[i])
            l2.append(items[(len(items) // 2) + i])
        return [l1, l2]
    elif len(items) % 2 != 0:
        l1 = []
        l2 = []
        for i in range(0, int(len(items) + 1) // 2):
            if i + 1 == (len(items) + 1) // 2:
                l1.append(items[i])
                break
            else:
                l2.append(items[((len(items) + 1) // 2) + i])
                l1.append(items[i])

        return [l1, l2]
    #return [items]


if __name__ == '__main__':
    print("Example:")
    print(split_list([1, 2, 3, 4, 5, 6]))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert split_list([1, 2, 3, 4, 5, 6]) == [[1, 2, 3], [4, 5, 6]]
    assert split_list([1, 2, 3]) == [[1, 2], [3]]
    assert split_list([1, 2, 3, 4, 5]) == [[1, 2, 3], [4, 5]]
    assert split_list([1]) == [[1], []]
    assert split_list([]) == [[], []]
    print("Coding complete? Click 'Check' to earn cool rewards!")
