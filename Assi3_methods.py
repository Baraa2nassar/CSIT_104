'''Question 1
1.   Write a Python program to calculate length and print
 the given string as a new string where the first and last 
 chars have been exchanged.
'''
s= str(input("Enter a string:"))
print ("The length of the string is:", len(s))
      
sstring = s[-1]+s[1:-1]+s[0]

print ("The resulted string:",sstring)

#**********************************************************
'''Question 2
2.   Takes input from the user and displays that input back in the following:
a)   Novel-upper case.
b)   Novel-lower case.
c)   Apply split() methodd()   
d) 	 Apply replace() ‘e’ with ‘&’ .
'''
Bo= input("What's your favotite novel?")
A= Bo.lower()
B= (Bo.upper())

print("My favourite novel is", A)
print("My favourite novel is", B)


      
line= input("Enter a Line:")
C= (line.split()) 
D= (line.replace('e','&'))
print ("The result string agter split is:", C)
print ("The result string agter split is:", D)

#**********************************************************
'''question 3
user will give three names for three states.
You will compare the names of the states and print them in alphabetic order.

'''

C1= input("Fircst State")
C2= input("Second State")
C3= input("Third State")

if C1[0]<C2[0]:
    print (C1, end=' ')
    if C2[0]<C3[0]:
       print(C2,end=' ')
       print(C3,end=' ')

    else:
       print(C3,end=' ')
       print(C2,end=' ')

if C2[0]<C1[0] and C2[0]<C3[0]:
   print(C2,end='')
   if C1[0]<C3[0]:
       print(C1,end=' ')
       print(C3,end=' ')
   else:
       print(C3,end=' ')
       print(C1,end=' ')

if C3[0]<C1[0] and C3[0]<C2[0]:
   print(C3,end=' ')
   if C1[0]<C2[0]:
       print(C1,end=' ')
       print(C2,end=' ')

   else:
       print(C2,end=' ')
       print(C1,end=' ')