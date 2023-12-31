# Write a Python program to get the Fibonacci series between 0 to 50

num1 = int(input("Enter number1 "))
num2 = int(input("Enter number2 "))
print (num1)
print (num2)
while num2<50:
    sum = num1+num2
    num1 = num2
    num2 = sum
    if sum>50:
        break
    print (sum)