def spoonerize(words):
    parts = words.split(" ")
    p1=parts[0][0]
    p2=parts[1][0]
    new = f"{p2}{parts[0][1:]} {p1}{parts[1][1:]}"
    return (new)

print(spoonerize("pop corn"))
