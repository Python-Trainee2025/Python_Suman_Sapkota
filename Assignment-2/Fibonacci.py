#1. Write a program that takes a number n and prints the first n numbers in the Fibonacci sequence. Use both Recursion and regular method

def fibonacci_recursive(n):
    if n == 0:
      return  0
    elif n == 1:
        return  1
    else:
        return fibonacci_recursive(n-1) + fibonacci_recursive(n-2)

def print_fibonacci_recursion(n):
    print("Fibonacci sequence using recursion:")
    for i in range(n):
        print(fibonacci_recursive(i),end="")
    print()

n= int(input("Enter the number of terms "))
print_fibonacci_recursion(n)

#using iterative method

def fibonacci_iterative(n):
    a,b = 0,1
    for _ in range(n):
        a,b = b,a+b
        print()
n= int(input("Enter the number of fibonacci terms "))
print_fibonacci_recursion(n)
