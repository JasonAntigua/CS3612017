print("Exercise 6: ");
print("Part A");

def is_prime(n):
        if n <= 1:
                return False;
        else:
                for p in range(2, n):
                        if n % p == 0:
                                return False;
                return True;

print("\nTest Values:");
print("Is 0 prime? : ", is_prime(0));
print("Is 7 prime? : ", is_prime(7));
print("Is 24 prime? : ", is_prime(24));
print("Is 41 prime? : ", is_prime(41));
print("Is 53 prime? : ", is_prime(53));
print("Is 100 prime? : ", is_prime(100));


print("\nPart B");

def is_prime(n):
        if n == 2 or n == 3:
                return True;
        if n % 2 == 0 or n % 3 == 0:
                return False;
        if n <= 1:
                return False;

        j = 5;
        k = 2;

        while j ** 2 <= n:
                if n % j == 0:
                        return False;
                j += k;
                k = 6 - k;
        return True;

print("\nTest values:");
print("Is 2 prime? : ", is_prime(2));
print("Is 14 prime? : ", is_prime(14));
print("Is 23 prime? : ", is_prime(23));
print("Is 47 prime? : ", is_prime(47));
print("is 72 prime? : ", is_prime(72));

print("\nPart C");

def primesUpTo(n):
        x = 0;
        while x <= n:
                if is_prime(x):
                        print(x);
                x += 1;
                
print("\nTesting function primesUpTo(n)");
print("All prime numbers up to 45: ",);
print(primesUpTo(45));

print("\nPart D");

def firstPrimes(n):

        total_primes = n;
        start_point = 2;
        while total_primes > 0:
                if is_prime(start_point):
                        total_primes = total_primes - 1;
                        print(start_point);
                start_point += 1;
                
print("\nTesting function firstPrimes(n)");
print("First 10 prime numbers: ");
print(firstPrimes(10));
