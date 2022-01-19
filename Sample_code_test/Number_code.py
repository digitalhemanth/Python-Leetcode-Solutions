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

# take input from the user
num = int(input("Enter a number: "))

# initialize sum
sum = 0

# find the sum of the cube of each digit
temp = num
while temp > 0:
   digit = temp % 10
   sum += digit ** 3
   temp //= 10

# display the result
if num == sum:
   print(num,"is an Armstrong number")
else:
   print(num,"is not an Armstrong number")
