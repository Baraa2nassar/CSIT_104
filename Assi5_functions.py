'''Q1
take two strings as parameters. 
First string will be your first name and second string is your last name.
print them
'''
def name (FirstName,LastName):
    print (FirstName,LastName)


name("Baraa","Nassar")


#That is my name :)

#------------------------------
'''Q2
unction where you can pass the values
for variables x and y as keyword arguments
and then the function will return the one 
which is bigger
'''
def larger (x,y):
    a= max (x,y) #max returns the largest among x, y
    print (a)

larger (0,2)
#-----------------------------------
'''Q3
ill declare two variables with same name: one will be global and another 
will be local inside a function. 
Then print the values of the variables both 
inside the function and outside the function 
and explain the output.
'''
def net ():         #Created a function
    MyMony=50      
     #Variable MyMony is local because it 
     #is inside the function. We know it from identations. 
    net1= MyMony/5  
    MyMony=net1     
    print (MyMony)  #Prints out 'MyMony' after it has been devided by 5
    
net()               #Makes the function work


MyMony=50           #The caiable MyMony here is global because it is not under
                    # any function and it is at the beging of the line.
print (MyMony)      #Prints out the global MyMoney
#------------------------------------
'''Q4
sum in cases; function that will return summation of two integers 
'''
#case a.
def sum1 (a,b):
    print (a+b)
sum1(1,2)           #you have to pass arguements here for case a


#case b.
def sum2 (a=5,b=5): #b&&a have set defoult of 5
    print (a+b)
sum2 ()


#case c.
def sum3 (a,b=5):   #b has a default set to 5
    print (a+b)
sum3 (1)


