'''Question 1
add odd numbers from 1 to 100
'''
sum=0 
for x in range (1,101):
    if x%2==0:
        continue 
    sum= sum+x
print(sum)
#-----------------------
'''Question 2
display the following pattern:
*
**
***
****
*****
******
'''
for i in range(1, 7):
    print("*"*i)
i+=1
#-------------------------------------------
'''Question 3
take input string from the user and print them until 
the user gives the string “Quit”. Use break.

'''
string=1
while string!=0:
    string= input ("enter somehting my friend")
    if  string == "quit":
        break
print (string)
#--------------------------------------------------
'''Question 4
write a program that will display a two dimensional
 table like the following using nested loop
 1 2 3 4 5
 1 2 3 4 5
 1 2 3 4 5
 1 2 3 4 5
 1 2 3 4 5
'''
j=1
while j<=5:
    for i in range (1,6):
        print (i, end=' ')
    print ("\r")
    j=j+1

   


