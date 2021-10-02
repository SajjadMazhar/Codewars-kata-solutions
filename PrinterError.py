def printer_error(s):
    error = 0
    for let in s:
        if let in colors:
            continue
        else:
            error += 1
    return error

    pass


string = 'ussllloooo'
colors = 'abcdefghijklm'
print(f"{printer_error(string)}/{len(string)}")
