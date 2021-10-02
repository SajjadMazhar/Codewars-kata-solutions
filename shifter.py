def shifter(string):
    if string == '':
        return 0
    else:
        llst = ["H", "I", "N", "O", "S", "X", "Z", "M", "W"]
        words = set(string.split(' '))
        counter = 0
        for word in words:
            for itr in range(len(word)):
                if word[itr] in llst:
                    continue
                break
            else:        
                counter+=1

        return counter

print(shifter(""))