def add():
    lst=[0,1,2,3,4,5,6,7,8,9]
    x=int(input("enter number to add ot the list"))
    z=lst.append(x)
    print(lst)

#------------------------------------
def remove():
    lst=[0,1,2,3,4,5,6,7,8,9]
    y=int(input("enter number to remove ot the list"))
    lst.remove(y)
    print(lst)
          
#------------------------------------
def main():
    lst=[0,1,2,3,4,5,6,7,8,9]
    print("This is your list: ", lst)
    while True:
        User_Input=int(input("please choose one of the following:\n1.Add Item\n2.Remove Item\n3.Quit"))
          
        if User_Input==1:
            add()
        elif User_Input==2:
            remove()
        elif User_Input==3:
                  break 

main()
#--------------------------------------------------
#Minute programm converts

seconds=int(input("enter seconds"))
minutes=seconds//60
remsec=seconds%60




print(minutes, "minute and", remsec, "seconds")



