
print("1.mdas")
print("2.detecting a prime number")
print("3.solve for a varible")
print("4.factoring square roots")
print("5.proportions")
print("6.converting decimal to fractions and percents")
print("7.converting fractions to decimals and percents")
print("8.converting percents to decimals and fractions")
print()


def mdas():
  choose = input("what do you want to calculate (+,-,*,/):")
  if choose == '+':
    a = (input("enter a number:"))
    b = (input("enter a number:"))

    sum = float(a)+float(b)
    print(f"sum = {sum}")

  elif choose == '-':
    a = (input("enter a number:"))
    b = (input("enter a number:"))

    subtract = float(a)-float(b)
    print(f"subtraction = {subtract}")

  elif choose == '*':
    a = (input("enter a number:"))
    b = (input("enter a number:"))

    mul = float(a)*float(b)
    print(f"mul = {mul}")

  elif choose == '/':
    a = (input("enter a number:"))
    b = (input("enter a number:"))

    div = float(a)/float(b)
    print(f"div = {div}")




def prime_numbers():
  prime_or_comp = 'prime'
  num = int(input("enter a number:"))
  for x in range(2,num):
    if num%x == 0:
      prime_or_comp='composite'
  print(f"{num} is {prime_or_comp} number.")



def square_roots():
    import math
    import sympy
    from sympy import symbols

    n = int(input("enter a number:"))


    upper_limit = math.floor(math.sqrt(n)) + 1 
    max_factor = 1 
    other_factor = 1 
    square_root = 1 


    for x in range(1, upper_limit): 
        if n % (x**2) == 0: 
            max_factor = x**2 


    other_factor = n/max_factor 

    square_root = int(math.sqrt(max_factor)) 
    other_factor = int(other_factor) 
    output = square_root*sympy.sqrt(other_factor) 


    print(output)


def solve_for_variable():
  import random
  
  def string_frac(in_string):
       if "/" in in_string:
           nd = in_string.split("/")
           n = float(nd[0])
           d = float(nd[1])
           ans = n/d
           return ans
       else:
          ans = float(in_string)
          return ans
  
  a = int(input("enter number for a:"))#randint(-10,10)
  b = int(input("enter number for b:"))#randint(-10,10)
  c = int(input("enter number for c:"))#randint(-10,10)
  eq = print(f"{a}x+{b}={c}")
  ans = float((c-b)/a)
  answer = (input("enter your ans:"))
  
  if round(string_frac(answer),2) == round(ans,2):
    print("correct!!")
  else:
    print("wrong!!")

  print(ans)

def proportions():
  n1 = int(input("enter a n1:"))
  d1 = int(input("enter a d1:"))
  n2 = int(input("enter a n2:"))
  d2 = int(input("enter a d2:"))


  if n1 == 0:
    n1 = (d1*n2)/d2
    print(f"n1 is  {n1}")
  elif d1 == 0:
    d1 = (n1*d2)/n2
    print(f"d1 = {d1}")
  elif n2 == 0:
    n2 = (d2*n1)/d1
    print(f"n2 = {n2}")
  elif d2 == 0:
    d2 = (n2*d1)/n1
    print(f"d2 = {d2}")



def decimal():
    digits = input("Enter a decimal number to convert: ")
    exponent = int(len(digits))-1
    n = float(digits)

    numerator = int(n*10**exponent)
    denominator = 10**exponent
    percent = n*100

    print(f"decimal = {digits}")
    print(f"decimal to fractions = {numerator}/{denominator}")
    print(f"decimal to percents = {percent}%")


def frac():
    fractions = input("enter a fraction:")
    if "/" in fractions:
      nd = fractions.split("/")
      n = float(nd[0])
      d = float(nd[1])
      num = n/d
      per = num*100
    print(f"fraction = {fractions}")
    print(f"fractions to decimal = {num}")
    print(f"fractions to percents is = {per}%") 

def perc():
    per = float(input("enter a percentage:"))
    decimal = per/100
    digits = str(decimal)
    exponent = int(len(digits))-1
    n = float(digits)

    numerator = int(n*10**exponent)
    denominator = 10**exponent
    fractions = (f"{numerator}/{denominator}")

    print(f"your percentage is {per}")
    print(f"percentage to decimal = {decimal}")
    print(f"percentage to fractions = {fractions}")

while True :
   choose = int(input("enter your choice(0 to quit):"))
   if choose == 1:
    mdas()
   elif choose == 2:
    prime_numbers()
   elif choose == 3:
    solve_for_variable()
   elif choose == 4:
    square_roots()
   elif choose == 5:
    perc()
   elif choose == 6:
    decimal()
   elif choose == 7:
    frac()
   elif choose == 8:
    perc()
   elif choose == 0:
     break
