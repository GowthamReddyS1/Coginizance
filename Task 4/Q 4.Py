print('Check weather a is palindrome or not')
number=int(input("Enter number:"))
duplicate=number
sum=0
while(number>0):
    rem=number%10
    sum=sum*10+rem
    number=number//10
if(duplicate==sum):
    print("The number is a palindrome!")
else:
    print("The number isn't a palindrome!")