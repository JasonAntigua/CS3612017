print("Exercise 11: ");

list1 = [1, 2, 3, 4, 5];
l1 = len(list1);
list2 = [6, 7, 8, 9, 10];
l2 = len(list2);


def recursion(list, i):
	if i == 0:
		return (list[i]);
	else:
		return (list[i] * recursion(list, i-1));

print("\nTesting two arrays for recursively getting the products of their elements");
print("\nContents of List 1: ", list1);
print("Product of List 1 using recursion: ", recursion(list1, l1-1));
print("\nContents of List 2: ", list2);
print("Product of the List 2 using recursion: ", recursion(list2, l2-1));

def iteration(list, i):
	product = 1;
	for x in range(i):
		product = product * list[x];
	return product;

print("\nTesting two arrays for getting the products of their elements through iteration");
print("\nContents of List 1: ", list1);
print("Product of List 1 using iteration: ", iteration(list1, l1));
print("\nContents of List 2: ", list2);
print("Product of the List 2 using iteration: ", iteration(list2, l2));
