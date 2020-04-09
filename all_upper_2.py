def is_all_upper(text: str) -> bool:
    # your code here
    if len(text.strip()) < 1 or text.isnumeric():
        return False
    for letter in text:
        if letter.islower():
            return False
    return True


if __name__ == '__main__':
    print("Example:")
    print(is_all_upper('ALL UPPER'))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert is_all_upper('ALL UPPER') == True
    assert is_all_upper('all lower') == False
    assert is_all_upper('mixed UPPER and lower') == False
    assert is_all_upper('') == False
    print("Coding complete? Click 'Check' to earn cool rewards!")
