print("Exercise 3: ");

print("\na. float(123) = ", float(123) );
print("This turns 123 into a float type and then prints it out.");

print("\nb. float('123') = ", float('123') );
print("This turns the input of '123' into a float and prints the actual value of 123 without the apostrophies");

print("\nc. float('123.23') = ", float('123.23'));
print("This turns the input of '123.23' into a float and prints it out wihout the apostrophies");

print("\nd. float(123.23) = ", float(123.23));
print("This turns the input 123.23 into a float type and then prints it out");

print("\ne. int(123.23)  = ", int(123.23));
print("This turns the input 123.23 into an int type and then prints out the value 123 instead since ints don't have decimals.");

print("\nf. int(float('123.23')) = ", int(float('123.23')));
print("This turns the input '123.23' into a float first and then into an int after, and then prints out the value which is 123.");

print("\ng. str(12)	= ", str(12));
print("This turns the input 12 into a string type and prints it out, so on screen the 12 is of type int now");

print("\nh. str(12.2) = ", str(12.2));
print("This tunrs the input 12.2 into a string type and then proceeds to print it");

print("\ni. bool('a') = ", bool('a'));
print("This turns a into a boolean type and then it prints out True meaning the it's a true bool type");

print("\nj. bool(0)	= ", bool(0));
print("This turns 0 into a boolean type and then printed out false, most likely because 0 always represents false and 1 represents true");

print("\nk. bool(0.1) = ", bool(0.1));
print("This turns the value 0.1 into boolean type and then printed out true");