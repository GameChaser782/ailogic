def solve(s):
    d = []
# the process here is to make a dict storing the number of times each unique letter is there in the initial string
# then we will use a separate dict to see that all the letters in the substrings (started from i location) are appended only once
# meanwhile we will keep appending the substring until the above requirement is satisfied
# once it dissatisfies, we count the total length of the substring and start with a new substring from i+1 location.
    tmp = d
    sub = s[0]

    return len(sub)

def main():
    s = "abcabcbb"
    return solve(s)