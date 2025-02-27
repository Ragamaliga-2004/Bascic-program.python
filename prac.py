# Swap two number
# a=int(input())
# b=int(input())
# a,b=b,a
# print(a,b)

# a=int(input())
# if a%2==0:
#     print("Even")
# else:
#     print("Odd")


# n=input()
# print(n[::-1])

# b=list(map(str,input().split()))
# print(b)

# Celsius=int(input())
# F=(Celsius*9/5)+32
# print(F)

# string=input()
# name=string[::-1]
# if string==name:
#     print("Palindrome")
# else:
#     print("Not a Palindrome")


# def palindrome(string):
#     return string==string[::-1]
# string=input()
# if palindrome(string):
#     print("Palindrome")
# else:
#     print("Not a Palindrome")

# a="Hello"
# b="World"
# print(a,b)

# a=int(input())
# b=int(input())
# c=float(input())
# result=(a+b)-c
# print(str(result)+" is the answer")

# a=int(input())
# if a<0:
#     print("Negative")
# elif a==0:
#     print("Zero")
# else:
#     print("Positive")

# a=int(input())
# b=int(input())
# c=int(input())
# if a>b:
#     print("A is greator")
#     if c>a:
#         print("c is greator")
# elif b>c:
#     print("B is greator")

# year=int(input())
# if (year%4==0 and year%100!=0) or (year%400==0):
#     print("Leap year")
# else:
#     print("Not Leap year")

# string=input()
# if (string=='a' or string=='e' or string=='i' or string=='o' or string=='u')and(string=='A' or string=='E' or string=='I' or string=='O' or string=='U'):
#     print("Vowel")
# else:
#     print("consonent")

# list=['Gfg','is','best','for','Geeks']
# for i in list:
#     res=i.replace('G','-').replace('e','G').replace('-','e')
#     print(str(i))

# list = input().split()
# llt = [word.replace('G', '#').replace('e', 'G').replace('#', 'e') for word in list]
# print(llt)

list = input().split()
for word in list:
b= word.replace('G', '#').replace('e', 'G').replace('#', 'e')
print(b)



