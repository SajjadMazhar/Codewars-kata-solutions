def over_the_road(address, n=3):
    if n<address:
        leftside = list(range(1, 2 * n + 1, 2))
        rightside = list(range(2 * n, 1, -2))

        for index in range(n):
            print(f"{leftside[index]}| ", end=' ')
            print(f" |{rightside[index]}")

        for index in range(n):
            if leftside[index] == address:
                print(rightside[index])
                break
            elif rightside[index] == address:
                print(leftside[index])
                break
    else:
        print("value of n should be not greater than address!")



add=int(input("enter the address: "))
n=int(input("enter n: "))

over_the_road(add, n)
