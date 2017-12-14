import re
print("Exercise 13: ");

file = open('emails.txt', 'r');
file = file.read();

emails = re.findall(r'([\w\S]+[@][a-z\S]+[.][a-z]+)', file);
print(emails);