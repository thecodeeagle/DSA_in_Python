def longest_substring_without_repeating(s):
    char_index = {}
    start = max_length = 0
    max_string = ""

    for i, char in enumerate(s):
        if char in char_index and char_index[char]>=start:
            start = char_index[char]+1
        char_index[char] = i
        if max_length < i-start+1:
            max_string = s[start:i+1]
        max_length = max(max_length, i-start+1)


    return max_length, max_string

def test_longest_substring():
    print(longest_substring_without_repeating("abcabcbb"))
    print(longest_substring_without_repeating("bbbbb"))


if __name__ == "__main__":
    test_longest_substring()