def solution(number):
    sum = 0
    for n in range(1, number):

        if n % 3 == 0 or n % 5 == 0:
            sum = sum + n

    return sum

print(solution(10))