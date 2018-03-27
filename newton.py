#Heron's Method for Calculating Square Roots
#Stub by JP Brichta, March 2018
#
#Heron's method for calculating square roots is approximately 2000 years old and was devised by Hero of Alexandria. It is an
#iterative method (meaning that it uses a previous answer to calculate the next) that in principle, will continue forever.
#When using iterative method, it is important to decide if the answer is "good enough" or if the program should continue.
#You can read more about Heron's Method and other methods of computing square roots in the wikipedia entry here:
#https://en.wikipedia.org/wiki/Methods_of_computing_square_roots#Babylonian_method
#

print("Order of input: Number to square root, rooted number guess")
print("No ones or zeros")

def newton(S, x):
  while abs(x**2  - S) > 0.001:
    x = x-((x**2-S)/(2*x))
  return round(x, 3)
