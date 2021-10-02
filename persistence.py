def persistence(n): #multiplies the individual digits given as n
    result = 1
    while n != 0:
        rem = n % 10
        result = result * rem
        n = n // 10
    return result #retruns single digit product


counter = 0
num = int(input("give integer: "))
if len(str(num)) == 1:
    print(counter)


else:
    newnum = persistence(num)
    counter += 1
    while True:
        if len(str(newnum)) > 1:
            newnum = persistence(newnum)
            counter += 1

        else:
            print(counter)

            break
