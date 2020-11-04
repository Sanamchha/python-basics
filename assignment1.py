def line():
	print("\n____________________________________________________________________________________\n")

###1
width = 17
height = 12.0
delimiter = '.'
print ("value for width/2 is \n -->{} which is of type : ".format(width/2), type(width/2)) 
print ("value for width/2.0 is \n -->{} which is of type : ".format(width/2.0), type(width/2.0)) 
print ("value for height/3 is \n -->{} which is of type : ".format(height/3), type(height/3)) 
print ("value for 1+2*5 is \n -->{} which is of type : ".format(1+2*5), type(1+2*5)) 
print ("value for delimiter*5 is \n -->{} which is of type : ".format(delimiter*5), type(delimiter*5)) 
line()


###2
f= float(input("enter the temperature in fahrenheit:"))
c= (f-32)/1.8
print("{}'F is {:.2f}'C".format(f,c))
line()



###3
sec= int(input("time in seconds"))
print ( "The entered time is equal to:\n ",int(sec/60),"minutes and ", (sec%60),"seconds"  )
line()



###4
_list = ["This", "is", "assignment","number",1]
print("Length =",len(_list))
print("1st element:    ",_list[0])
print("4th element:    ",_list[3])
line()

####5
string = "Hope you liked the code"
_list = list(string)
print("Before poping:",_list)
print("After  POP:",_list.pop(),"\n",_list)
print("After  POP of 6th element:",_list.pop(5),"\n",_list)
_list.insert(5,101)
print("After inserting a number at 5 position \n",_list)
_list.remove(101)
print("After Removing the inserted number \n",_list)
line()

