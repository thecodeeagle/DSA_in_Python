def is_palindrome(s):
    s = ''.join(filter(str.isalnum, s)).lower()
    return s == s[::-1]

def test_is_palindrome():
    print(is_palindrome("A man, a plan, a canal: Panama"))
    print(is_palindrome("race a car"))


if __name__ == "__main__":
    test_is_palindrome()
