def number_length(a: int) -> int:
    # your code here
    i = 1
    while True:
        if a // (10 ** i) != 0:
            i = i + 1
        else:
            return i
            break


if __name__ == '__main__':
    print("Example:")
    print(number_length(101))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert number_length(10) == 2
    assert number_length(0) == 1
    assert number_length(4) == 1
    assert number_length(44) == 2
    print("Coding complete? Click 'Check' to earn cool rewards!")
