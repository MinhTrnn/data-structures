def hello(count):
    #base case
    if count == 5:
        return
    print("Hello")
    hello(count + 1)

def factorial(n):
    if n == 1: # base case
        return 1
    result = factorial(n - 1) * n
    return result

def power_of_number(n,p):
    if p < 0:
        return 1/power_of_number(n, -p)
    if p == 0:
        return 1
    return power_of_number(n, p - 1) * n

def fibonacci(n):
    if n < 0:
        return -1 # return false value
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

def sum_of_digits(n):
    if n < 0:
        return sum_of_digits(-n)
    if n == 0: # base case
        return 0
    return n%10 + sum_of_digits(n//10)

def reverse_string(string):
    if len(string) == 0:
        return string
    return reverse_string(string[1:]) + string[0]

if __name__ == "__main__":
#     hello(0)
    string = "hello"
    print(reverse_string(string))