print("Exercise 9: ");

def merging_sublists(list):

	newList = [];
	for i in list:
		try:
			i = int(i);
			newList.append(i);
		except:
			for j in i:
				newList.append(j);
	return (newList);

listA = [[1, 2, 3], [4, 5]];
listB = [6, 12, 18, 24];
listC = [[1, 3], [3, 6]];
listD = [[10, 15, 20, 25], 30, 35];
print("\nList A: ", listA);
print("\nList A after funtion: ", merging_sublists(listA));
print("\nList B: ", listB);
print("\nList B after function: ", merging_sublists(listB));
print("\nList C: ", listC);
print("\nList C after function: ", merging_sublists(listC));
print("\nList D: ", listD);
print("\nList D after function: ", merging_sublists(listD));