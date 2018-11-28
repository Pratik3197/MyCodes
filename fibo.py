def fibonacci(n):
     #Return a list containing the Fibonacci series up to n.
     result = []
     a, b = 0, 1
     while b < n:
         result.append(b)    
         a, b = b, a+b
     return result
print(fibonacci(int(input("How many terms? \n"))))  # calling the func and printing the answer.