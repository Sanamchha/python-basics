#Exercise 1
##print("the prime numbers between 1 and 100 are:")
##for i in range(1,100):
    if i > 1:
        for j in range(2,i):
           if (i%j) == 0:
                break
        else:
            print(i)

"""-------------------------------------------------"""
#Exercise 2
string = input("Enter any string:")
reverse_string = string[::-1]

if string == reverse_string:
    print("{} is a palindrome" .format(string))
else:
    print("{} is not a palindrome" .format(string))

"""--------------------------------------------------------"""
#Exercise 3
string = input("Enter any string:")

upper = 0
lower = 0
digits = 0
sps = 0
for i in string:
    if (i.isupper()):
        upper += 1
    elif (i.islower()):
        lower += 1
    elif (i.isnumeric()):
        digits += 1
    else:
        sps += 1

print("the uppercases in {} are:".format(string), upper)
print("the lowercases in {} are:".format(string), lower)
print("the digits in {} are:".format(string), digits)
print("the special symbols in {} are:".format(string), sps)

"""-------------------------------------------------------------"""
#Exercise 4
n = int(input("Enter the number of terms:"))
sum = 0

print("the harmonic series for {} terms is:".format(n))
for i in range(1,n):
    print(round(1/i,2), end=" ")
    sum += 1/i

print()
print("the sum of harmonic series for {} terms is:".format(n), round(sum,2))

"""--------------------------------------------------------------------"""
#Exercise 5
for i in range(1, 6):
	for x in range(i, 5):
		print(' ', end=' ')
	for j in range(i):
		print('*', end=' ')
	print()

"""------------------------------------------------------------"""
#Exercise 6
Count = dict()
str = input("Enter any string:")
for i in range(len(str)):
	cnt = 0
	for j in range(len(str)):
		if str[i] == str[j]:
			cnt += 1
	Count[str[i]] = cnt
			
       
print(Count)

