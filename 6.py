x = input("Enter a phrase: ")
x = x.lower().replace(" ", "")
if x == x[::-1]:
    print("The entered phrase is a palindrome.")
else:
    print("The entered phrase is not a palindrome.")
