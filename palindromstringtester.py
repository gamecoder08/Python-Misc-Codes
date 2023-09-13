string= input("Enter a string: ")
string1=string.lower()
reverse_string = string1[::-1]

if string1 == reverse_string:
    print(f"{string} is a palindrome")
else:
    print(f"{string} is not a palindrome")