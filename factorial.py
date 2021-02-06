def factorial_recursive(number):
    if number <= 1:
        return 1
    else:
        return number * factorial_recursive(number-1)


def factorial_iterative(number):
    answer = 1
    for i in range(1, number+1):
        answer *= i

    return answer

print("Recursive Factorial")
print(factorial_recursive(5))
print("Iterative Factorial")
print(factorial_iterative(4))