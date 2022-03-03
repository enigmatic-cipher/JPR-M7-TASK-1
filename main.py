"""
Given a number n as input, print Hello n times. Use recursion. Do not use loops. Do a dry run for each test case.
Input-> 3
Output->
Hello
Hello
Hello
"""

def recur(n):
  print("Hello")
  if (n>1):
    recur(n-1)

n=3
recur(n)