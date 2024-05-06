Problem Statement: Anagram Detector

An anagram is a word or phrase formed by rearranging the letters of another word or phrase, typically using all the original letters exactly once. For example, the words "listen" and "silent" are anagrams of each other.

Write a Python function called is_anagram that takes two strings as input and returns True if the two strings are anagrams of each other, and False otherwise.

Function Signature:

python
Copy code
def is_anagram(str1: str, str2: str) -> bool:
pass
Input:

Two strings str1 and str2 containing only lowercase alphabets and/or spaces.
Output:

A boolean value indicating whether str1 is an anagram of str2.
Example:

python
Copy code

> > > is_anagram("listen", "silent")
> > > True
> > > is_anagram("hello", "world")
> > > False
> > > is_anagram("evil", "vile")
> > > True
> > > Note:

Treat spaces as characters and ignore them when determining if two strings are anagrams.
The input strings will not contain any special characters or uppercase letters.
