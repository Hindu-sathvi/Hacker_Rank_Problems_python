 #https://www.hackerrank.com/challenges/re-start-re-end/problem?isFullScreen=true
 #re-start-re-end
 #code
 #Enter your code here. Read input from STDIN. Print output to STDOUT
import re

def find_substring_indices(s, k):
    matches = list(re.finditer(r'(?={})'.format(re.escape(k)), s))
    if matches:
        for match in matches:
            start_index = match.start()
            end_index = start_index + len(k) - 1
            print(f"({start_index}, {end_index})")
    else:
        print("(-1, -1)")
if __name__ == "__main__":
    s = input()
    k = input()
    find_substring_indices(s, k)
"""
>import re-it is used to work with the regular expressions in python
>we Use re.finditer to find all matches of k in s
>Use the start() and end() methods of the match object to get the start and end indices of each match.
>re.finditer finds all non-overlapping matches of the pattern in s.
re.escape(k) escapes any special characters in k to ensure it is treated as a literal string.
(?={}) is a lookahead assertion to find starting positions of k in s.
"""