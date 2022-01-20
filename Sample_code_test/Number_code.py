#1. Python Program to Reverse a Number

def numres(num : int) -> int:
    reversed_num = 0
    while num != 0:
        digit = num % 10
        reversed_num = reversed_num * 10 + digit
        num //= 10    
    
    return reversed_num

print(numres(12345))


#2. Python Program to Reverse a number using sclicing 

number  = 11211
if str(number) == str(number)[::-1]:
    print(number)
else:
    print('Not a palindrom')
    
    
    
    
# Python program to check if the number is an Armstrong number or not

num = 153
sum = 0
tmp = num
while tmp>0:
    digit = tmp%10
    sum = sum+digit**3
    tmp //=10
if num==sum:
    print(num)
else:
    print("Try again")
    
def find_armstrong():
    arm = []
    for i in range(100000):
        tmp = i
        sum = 0 
        while tmp>0:
            digit= tmp%10
            sum=sum+digit**3
            tmp //= 10
        if i == sum:
           arm.append(i)
    return(arm)

print(find_armstrong())
        
        
#A positive integer greater than 1 which has no other factors except 1 and the number itself is called a prime number. 2, 3, 5, 7 etc.

num = 7

for i in range(2,num+1):
    if num % i == 0:
        print("Its prime")
    else:
        print("not prime")
     
        
    