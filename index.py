#1.add two numbers

num1 = float (input("enter number 1: "))
num2 = float (input("enter number 2: "))

sum = num1+num2
print(sum)

#2 check condition 
a = int (input("enter value of a: "))
b = int (input("enter value of b: "))

if (a % 10 == 0 and b % 10 == 0):
    print ("true")
elif (a % 10 == 0 and b % 10 == 0):
    print ("true")   
else:
    print("false")     

#3 find the first digit of a 4 digit number 

num1 = int(input("enter your 4 digit number: "))
ans = num1 // 1000
print (ans) 


#4 find the last digit of a 4 digit number 
num1 = int(input("enter 4 digit number: "))
ans = num1 % 10
print (ans)

#5. find the remainder when num1 divided by num2
num1 = float (input("enter number 1: "))
num2 = float (input("enter number 2: "))

rem = num1 % num2
print(rem)

#6. multiply two numbers
num1 = int (input("enter number 1: "))
num2 = int (input("enter number 2: "))

mul = num1 * num2
print(mul)

#7. marks calculator
marks1 = float(input("enter marks1: "))
marks2 = float(input("enter marks2: "))
marks3 = float(input("enter marks3: "))

total = marks1 + marks2 +marks3
avg = ((marks1 + marks2 +marks3)/3)

print ("total marks: ",total)
print ("average marks: ",avg)


























