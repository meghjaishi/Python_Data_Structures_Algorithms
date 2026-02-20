# fibonacci function with time complexity O(2^n)
counter = 0

def fib_recursive(n):
    global counter
    counter += 1
    if n == 0 or n == 1:
        return n
    return fib_recursive(n-1) + fib_recursive(n-2)

def fib_memo(n, memo={}):
    global counter
    counter += 1
    if n in memo:
        return memo[n]
    
    if n == 0 or n == 1:
        return n
    memo[n] = fib_memo(n-1, memo) + fib_memo(n-2, memo)
    return memo[n]

def fib_iter(n): # Iterative process reduces time complexity to O(n)
    fib_list = [0,1]
    global counter
    for index in range(2, n+1):
        counter += 1
        next_fib = fib_list[index - 1] + fib_list[index - 2]
        fib_list.append(next_fib)
    return fib_list[n]

def fib_iter_memo(n): # Iterative process with memoization reduces time complexity to O(n) and space complexity to O(1)
    if n == 0 or n == 1:
        return n
    
    prev, curr = 0, 1
    global counter
    for index in range(2, n+1):
        counter += 1
        next_fib = prev + curr
        prev, curr = curr, next_fib
    return curr

if __name__ == "__main__":
    print(fib_recursive(35))
    print("Number of calls:", counter)
    counter = 0  # Reset counter for memoized version
    print(fib_memo(35))
    print("Number of calls with memoization:", counter)
    counter = 0  # Reset counter for iterative version
    print(fib_iter(35))
    print("Number of iterations in iterative version:", counter)
    counter = 0  # Reset counter for iterative memoized version
    print(fib_iter_memo(35))
    print("Number of iterations in iterative memoized version:", counter)


