# 1.2 Write curry2 as a lambda function

curry2 = lambda h: lambda x: lambda y: h(x, y)

#1.5  Write a function that takes in a function cond and 
#     a number n and prints numbers from 1 to n where 
#     calling cond on that number returns True.

def keep_ints(cond, n):
  """Print out all integers 1..i..n where cond(i) is true

  >>> def is_even(x):
  ...  # Even numbers have remainder 0 when divided by 2.
  ...  return x % 2 == 0
  >>> keep_ints(is_even, 5)
  2
  4
  """
  i = 1
  while i <= n:
    if cond(i):
      print(i)
    i += 1

# 1.6 Write a function similar to keep_ints like before, 
#     but now it takes in a number n and returns a function 
#     that has one parameter cond. The returned function prints 
#     out numbers from 1 to n where calling cond on that number

def make_keeper(n):
  """Returns a function which takes one parameter cond and prints out
all integers 1..i..n where calling cond(i) returns True.

  >>> def is_even(x):
  ...   # Even numbers have remainder 0 when divided by 2.
  ...   return x % 2 == 0
  >>> make_keeper(5)(is_even)
  2
  4
  """
  def check_cond(cond):
    i = 1
    while i <= n:
      if cond(i):
        print(i)
      i += 1
  return check_cond

#   1.7 Write a function and add that takes a one-argument function 
#       f and a number n as arguments. It should return a function 
#       that takes one argument, and does the same thing as the function 
#       f, except also adds n to the result.

def and_add(f, n):
  """Return a new function. This new function takes an argument x and returns f(x) + n.

  >>> def square(x):
  ...   return x * x
  >>> new_square = and_add(square, 3)
  >>> new_square(4)  # 4 * 4 + 3
  19
  """

  return lambda x: f(x) + n
