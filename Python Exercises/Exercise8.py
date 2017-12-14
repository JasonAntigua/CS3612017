print("Exercise 8: ");

print("\nPart A: ");
a = [5, 10, 15, 20];
print("\nPrinting the contents of list a: ", a);

print("\nPart B: ");

b = a;

print("\nWe set b = a, so what gets printed is: ", b);
print("Which is the exact same array as 'a'. ");

print("\nPart C & D: ");

b[1] = 25;

print("\nWe changed b[1] to equal 25, so we will print out the contents of both lists: ");
print("\nContents of list b: ", b);
print("\nContents of list a: ", a);
print("\nAs you can see the changes made to list b also affect the contents of list a.\nSo both of their index 1 values got changed.");

print("\nPart E: ");

c = a[:];

print("\nWe set c equal to a[:], and so we will print its content to see what it did. ", c);

print("\nPart F & G: ");

c[2] = 30;

print("\nWe made c[2] equal to 30, so we will print the list of a & c to see any changes: ");
print("\nContents of A: ", a);
print("\nContents of C: ", c);

print("\nPart H: ");

def set_first_elem_to_zero(l):
	l[0] = 0;
	return(l);

oList = [2, 4, 6, 8];
print("\nWe will be using a funtion to transform a list's first entry to 0.");
print("\nOriginal List: ", oList);
print("\nList after function: ", set_first_elem_to_zero(oList));
