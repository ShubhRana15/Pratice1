def is_palindrome(word):
    """Return True if word is a palindrome, False if not."""
    return word == word[::-1]

print(is_palindrome("foo"))
print(is_palindrome("racecar"))
print(is_palindrome("troglodyte"))
print(is_palindrome("civic"))

def is_palindrome_recur(word):
    """Return True if word is a palindrome, False if not."""
    if len(word) <= 1:
         return True
    else:
        return word[0] == word[-1] and is_palindrome(word[1:-1])

print(is_palindrome_recur("foo"))
print(is_palindrome_recur("racecar"))
print(is_palindrome_recur("troglodyte"))
print(is_palindrome_recur("civic"))