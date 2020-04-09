def correct_sentence(inp_sentece):
    outputS = inp_sentece
    #print(inp_sentece[0])
    if inp_sentece[0].islower():
        outputS = inp_sentece[0].upper() + inp_sentece[1:]
    if inp_sentece[-1] != '.':
        outputS = outputS+'.'
    return outputS
print(correct_sentence(input()))