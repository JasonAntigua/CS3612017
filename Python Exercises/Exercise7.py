print("Exercise 7: ");

listOne = [1, 3, 5, 7, 9, 11] 
listTwo = [2.2, 4.4, 6.6, 8.8, 10.10]

def printArray(list):

	for x in range (len(list)):
		print(list[x]);

print("\nPart A: ");
print("\nPrinting list One: ");
printArray(listOne);
print("\nPrinting list two: ");
printArray(listTwo);

def reverseArray(list):

	for x in list[::-1]:
		print(x);

print("\nPart B: ")
print("\nPrinting list one in reverse: ");
reverseArray(listOne);
print("\nPrinting list two in reverse: ");
reverseArray(listTwo);

def myLenFuntion(list):

	countList = 0; 
	for x in list:
		countList += 1;
	return(countList);

print("\nPart C: ");
print("\nPrinting the length of list one: ", myLenFuntion(listOne));
print("\nPrinting the length of list two: ", myLenFuntion(listTwo));