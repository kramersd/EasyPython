#Author: Shane Kramer
#Date: 10/5/2017
#Descpt: General Fizz Buzz
#        maxNum: The max number to print to
#        f1, w1: First mulitple to replace, word to replace multiple with
#        f2, w2: Second multiple to replace, word to replace multiple with

maxNum = int( input("Enter the max number: "))
f1, w1 = input("Enter a factor and word: ").split(' ')
f2, w2 = input("Enter a factor and word: ").split(' ')

f1 = int(f1)
f2 = int(f2)

for x in range(1, maxNum + 1):
     y = 0
    if(x % f1 == 0 and x % f2 == 0):
        print(w1, end="")
        y = 1
    elif(x % f1 == 0):
        print(w1)
        y = 1
    
    if(x % f2 == 0):
        print(w2, end="\n")
        y = 1

    if(y==0):
        print(x)

        
    
