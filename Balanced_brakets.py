#https://www.hackerrank.com/challenges/balanced-brackets/problem?isFullScreen=true
#code:
def isBalanced(s):
    # Write your code here
    stack = []
    match = {'(': ')', '{': '}', '[': ']'}
    
    for ch in s:
        if ch in match:
            stack.append(ch)
        else:
            if not stack or match[stack.pop()] != ch:
                return "NO"
    if not stack:
        return "YES"
    else:
        return "NO"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        s = input()

        result = isBalanced(s)

        fptr.write(result + '\n')

    fptr.close()
