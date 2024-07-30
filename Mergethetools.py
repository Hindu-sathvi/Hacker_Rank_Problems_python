#https://www.hackerrank.com/challenges/merge-the-tools/problem?isFullScreen=true
#merge-the-tools
#code
def merge_the_tools(string, k):
    # your code goes here
    for i in range(0, len(string), k):#it divides the given string into k no.of parts
        t = string[i:i + k]#we get the substring of length k
        u = ''.join(dict.fromkeys(t))#This line creates a new string u from t where all duplicate characters are removed, and the original order of characters is preserved.


        print(u)
if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)