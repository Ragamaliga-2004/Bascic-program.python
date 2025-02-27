Write a Python program to swap the values of two variables without using a temporary variable.
a=int(input())
b=int(input())
a,b=b,a
print(a,b)

Write a Python program that takes an integer as input and prints whether it is even or odd.
a=int(input())
if a%2==0:
    print("Even")
else:
    print("Odd")

Write a reverse number program
n=input()
print(n[::-1])

Write a Python program that converts a temperature in Celsius to Fahrenheit. Take the Celsius temperature as input from the user.
Celsius=int(input())
F=(Celsius*9/5)+32
print(F)

Write a Python without using function to reverse a given string and return the reversed string.
string=input()
name=string[::-1]
if string==name:
    print("Palindrome")
else:
    print("Not a Palindrome")

Write a Python function to reverse a given string and return the reversed string.
def palindrome(string):
    return string==string[::-1]
string=input()
if palindrome(string):
    print("Palindrome")
else:
    print("Not a Palindrome")

Given three variables: `a = ‘100’`, `b = 25`, and `c = ‘10.5’`, write a Python program to perform the following operations and print the results: – Convert `a` to an integer and add it to `b`. – Convert `c` to a float and subtract it from the result of the first operation. – Convert the final result to a string and concatenate it with the string ” is the answer.”
a=int(input())
b=int(input())
c=float(input())
result=(a+b)-c
print(str(result)+" is the answer")

Write a Python program that takes a number as input and prints whether it is positive, negative, or zero.
a=int(input())
if a<0:
    print("Negative")
elif a==0:
    print("Zero")
else:
    print("Positive")

Write a Python program that takes three numbers as input and prints the largest among them.
a=int(input())
b=int(input())
c=int(input())
if a>b:
    print("A is greator")
    if c>a:
        print("c is greator")
elif b>c:
    print("B is greator")

Write a Python program that takes a year as input and determines if it is a leap year or not.
year=int(input())
if (year%4==0 and year%100!=0) or (year%400==0):
    print("Leap year")
else:
    print("Not Leap year")

Write a Python program that takes a single character as input and determines whether it is a vowel or a consonant.
string=input()
if (string=='a' or string=='e' or string=='i' or string=='o' or string=='u')and(string=='A' or string=='E' or string=='I' or string=='O' or string=='U'):
    print("Vowel")
else:
    print("consonent")

Replace the words in string
list = input().split()
res = []
for sub in list:
    modified_word = sub.replace('G', '-').replace('e', 'G').replace('-', 'e')  
    res.append(modified_word)  
print(res)







