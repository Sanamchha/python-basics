###1
random = [1,3,5,2,6,7]
total=0
for x in range(len(random)):
	total += random[x]
print ("The sum of ",random,"elements is ",total)

###2
def common(a,b):
	l1 = set(a)
	l2 = set(b) 
	same=list((l1.intersection(l2)))

	return same

list1 = [1,22,33,44,55,66]
list2 = [99,33,75,34,22,66,88]
print("The common elements between ",list1," and  ",list2," are : ",common(list1,list2))


###3
_list = [1,5,7,12,15]
for x in range(len(_list)):
	print(_list[x],_list[x]*_list[x])


###4
string = input("Enter any words: ")
print("THE ENTERED STRING IS: ",string)
count= 0 
for i in string:
	# print(i)
	count += 1
print("Total letters count is: ",count)

###5
string = input("Enter any words:")
print(string.upper())
print(string.lower())