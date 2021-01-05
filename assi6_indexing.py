'''Question 1

'''

lst= ["Red","Green","White","Black","Pink","Yellow"]
print ("items in the list:", lst)   #prints the orignal string


lst.append("Orange") #adds orange to the end of the list
print ("items in the list after appending:", lst)

lst.remove("Pink") #'remove' deletes the variable-not index- that was assighned 
print("items in the list after deleting:", lst)


lst.reverse()
print("items in the list after reverse:", lst)



#-------------------------------------
'''Question 2

'''

lst=[1,2,3,4,5]     #creating "lst"

print (lst[1])      #Select the second item in the list.

print (lst[-2])     #The second to last item in the list.  

print (lst[:])      #slicing the whole list

print (lst[1:-1])   #Slicing to select from the second item to the fourth item in the list.
