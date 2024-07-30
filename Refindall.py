#https://www.hackerrank.com/challenges/re-findall-re-finditer/problem?isFullScreen=true
#re-findall-re-finditer
#code
# Enter your code here. Read input from STDIN. Print output to STDOUT+++++++++++
import re

def find_vowel_substrings(s):
    # Define the pattern
    pattern = r'(?<=[qwrtypsdfghjklzxcvbnmQWRTYPSDFGHJKLZXCVBNM])[aeiouAEIOU]{2,}(?=[qwrtypsdfghjklzxcvbnmQWRTYPSDFGHJKLZXCVBNM])'
    
    # to find all matches using re.findall()
    matches = re.findall(pattern, s)
    if matches:
        for match in matches:
            print(match)
    else:
        print(-1)
if __name__ == "__main__":
    s = input()
    find_vowel_substrings(s)
