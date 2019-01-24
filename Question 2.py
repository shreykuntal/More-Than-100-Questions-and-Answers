#Question:
#Write a program which can compute the factorial of a given numbers.
#The results should be printed in a comma-separated sequence on a single line.
#Suppose the following input is supplied to the program:
#8
#Then, the output should be:
#40320


#Answer
num = int(input('Enter an integer: '))
factorial = 1
for i in range(2, num+1):
    factorial *= i
print(str(num)+'! = '+str(factorial))