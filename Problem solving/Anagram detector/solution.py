def is_anagram(s1, s2):
    # Remove spaces and convert to lowercase
    s1 = s1.replace(" ", "").lower()
    s2 = s2.replace(" ", "").lower()
    
    # Check if the sorted strings are equal
    return sorted(s1) == sorted(s2)

# Read the two strings from input
s1 = input().strip()
s2 = input().strip()

# Call the function and print the result
print(is_anagram(s1, s2))
