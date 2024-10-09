def fibonacci(n):

  a=0
  b=1
  count = 0

  while count < n:
    print(a, end=" ")
    a, b = b, a + b
    count += 1

fibonacci(20) 