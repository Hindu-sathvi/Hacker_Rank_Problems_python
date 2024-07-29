#https://www.hackerrank.com/challenges/swap-case/problem?isFullScreen=true
#swap-case
#code
def swap_case(s):
    return s.swapcase()#swapcase() function is used to  convert all lowercase letters to uppercase letters and vice versa.
if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)