def is_palindrome(s):
    # Remove spaces, punctuation, and convert to lowercase
    s = ''.join(char.lower() for char in s if char.isalnum())
    
    # Check if the string is equal to its reverse
    return s == s[::-1]

# Read the string from input
s = input().strip()

# Call the function and print the result
print(is_palindrome(s))
