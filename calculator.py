what = input("Что делаем? (+,-,*,/): ")
a = float(input("Первое число "))
b = float(input("Второе число "))
import sys
class Calculator:
       if what == "*":
          def multiply(a, b):
             return a * b
          print(multiply(a,b))
       elif what == "+":
          def addition(a,b):
             return a+b
          print(addition(a,b))
       else:
          print("Choose right option!")