def cut_sentence(line, length):
    '''
    Cut a given sentence, so it becomes shorter than or equal to a given length.
    '''
    if len(line) <= length:
        return line
    elif length <= line.find(" "):
        return "..."
    else:
        if line[length:length+1].isalpha():
            #print("cepr duma")
            #print(line[:length])
            tempLine = line[:length]
            #print(line[:len(line) - line[::-1].find(" ")])
            return tempLine[:len(tempLine) - tempLine[::-1].find(" ")].strip() + "..."
        else:
            return(line[:length] + "...")
    return line[:length]

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    #assert cut_sentence("Hi my name is Alex", 4) == "Hi...", "First"
    #assert cut_sentence("Hi my name is Alex", 10) == "Hi my...", "Second"
    print(cut_sentence("Hello my name is Alex", 3))
    #assert cut_sentence("Hi my name is Alex", 18) == "Hi my name is Alex", "Third"
    #assert cut_sentence("Hi my name is Alex", 20) == "Hi my name is Alex", "Fourth"
    print('Done! Do you like it? Go Check it!')
