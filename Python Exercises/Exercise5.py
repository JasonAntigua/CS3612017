print("Exercise 5: ");

print("\nThis exercise finds the first 20 numbers that are" + 
        " divisible by 5, 7 & 11 and prints them");

def firstTwenty():

        number_found = 0;
        x = 11; 

        while number_found < 20: 
                divide_five = (x % 5 == 0);
                divide_seven = (x % 7 == 0);
                divide_eleven = (x % 11 == 0);

                if divide_five and divide_seven and divide_eleven == True:
                        print(x);
                        number_found += 1;
                x += 1;

print("\nThe first 20 numbers are: ");
firstTwenty();
