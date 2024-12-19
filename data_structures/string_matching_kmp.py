# O(m+n) complexity

def compute_lps(pattern):
    lps = [0]*len(pattern)
    length = 0
    i = 1
    while i < len(pattern):
        if pattern[i] == pattern[length]:
            length+=1
            lps[i] = length
            i+=1
        elif length !=0:
            length = lps[length-1]
        else:
            lps[i]=0
            i+=1
    return lps

def kmp_search(text, pattern):
    lps = compute_lps(pattern)
    print(lps)
    i = j = 0
    result = []

    while i<len(text):
        if text[i] == pattern[j]:
            i+=1
            j+=1
        if j == len(pattern):
            result.append(i-j)
            j = lps[j-1]
        elif i < len(text) and text[i]!=pattern[j]:
            if j!=0:
                j = lps[j-1]
            else:
                j=0
                i+=1
    return result


def test_kmp_search():
    print(kmp_search("ababcabcabababd", "ababd"))

if __name__ == "__main__":
    test_kmp_search()

