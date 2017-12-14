print("Exercise 12: ");

def fibonacci(n):
	if n <= 1:
		return n;
	else:
		return fibonacci(n-1) + fibonacci(n-2);

print("\nTesting the fibonacci funtion:");
print("6th Fibonacci Number: ", fibonacci(6));
print("9th Fibonacci Number: ", fibonacci(9));
print("12th Fibonacci Number: ", fibonacci(12));