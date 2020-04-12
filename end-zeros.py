def end_zeros(num: int) -> int:
    # your code here
    NormalS = str(num)
    if num == 0:
        return 1
    else:
        if len(NormalS) == len(str(int(NormalS[::-1]))):
            return 0
        else:
            return len(NormalS) - len(str(int(NormalS[::-1])))


if __name__ == '__main__':
    print("Example:")
    print(end_zeros(0))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert end_zeros(0) == 1
    assert end_zeros(1) == 0
    assert end_zeros(10) == 1
    assert end_zeros(101) == 0
    assert end_zeros(245) == 0
    assert end_zeros(100100) == 2
    print("Coding complete? Click 'Check' to earn cool rewards!")
