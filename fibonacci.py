def fibonacci_recursive(n):
    if n <= 1:
        return n 
    else:
        return fibonacci_recursive(n-1) + fibonacci_recursive(n-2)

def fibonacci_iterative(n):
    answer = [0, 1]
    for i in range(2, n+1):
        answer.append(answer[i-1] + answer[i-2])
    
    return answer[n]

# Testing
print("Recursive Fibonacci")
print(fibonacci_recursive(8))

print("Iterative Fibonacci")
print(fibonacci_iterative(8))