def first_word(input_string):
    wordsL = input_string.split()
    for el in range(0,len(wordsL)-1):
        if wordsL[el] == '.':
            wordsL.pop(el)
    print(wordsL)
    return wordsL[0].capitalize()

print(first_word("  . alabala portu kala mala"))