print("This is a python program for the hacktober fest 2020 ")
# Program to check if a number is prime or not

num = 407

# To take input from the user
#num = int(input("Enter a number: "))

# prime numbers are greater than 1
if num > 1:
   # check for factors
   for i in range(2,num):
       if (num % i) == 0:
           print(num,"is not a prime number")
           print(i,"times",num//i,"is",num)
           break
   else:
       print(num,"is a prime number")
       
# if input number is less than
# or equal to 1, it is not prime
else:
   print(num,"is not a prime number")
   
# import complex math module  
import cmath  
a = float(input('Enter a: '))  
b = float(input('Enter b: '))  
c = float(input('Enter c: '))  
  
# calculate the discriminant  
d = (b**2) - (4*a*c)  
  
# find two solutions  
sol1 = (-b-cmath.sqrt(d))/(2*a)  
sol2 = (-b+cmath.sqrt(d))/(2*a)  
print('The solution are {0} and {1}'.format(sol1,sol2)) 

def my_function(x):
  return x[::-1]

mytxt = my_function("I wonder how this text looks like backwards")

print(mytxt)
#armstrong number
num = int(input("Enter a number: "))  
sum = 0  
temp = num  
  
while temp > 0:  
   digit = temp % 10  
   sum += digit ** 3  
   temp //= 10  
  
if num == sum:  
   print(num,"is an Armstrong number")  
else:  
   print(num,"is not an Armstrong number")  
