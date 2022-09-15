num = input("Enter first number:")
num1 = input("Enter second number:")

if num.isnumeric and num1.isnumeric():
      a=int(num)
      b=int(num1)
      x=input("please enter operators:")
      print("Both are numeric")
      if x == "+":
          print("Addition",a+b)
      elif x == "-":
          print("subtraction",a-b)
      elif x == "*":
          print("Multiplication",a*b)
      elif x == "/":
          print("Division",a/b)
      elif num.isalpha or b.isnumeric():
          print("Both are not same")
elif num.isalpha and num1.isalpha():
    print("Both are Alphabet")
else:
    print("Both are not same")
    
#elif num.isalpha or num1.isalpha():
#    print("Both are same conditions")

#elif num.isalpha and num1.isnumeric()==num.isnumeric and num1.isalpha():
#    print("Both are Alphabet")

#elif a.isalpha and num1.isnumeric()==num.isnumeric and num1.isalpha():
#    print("Both are Alphabet")
