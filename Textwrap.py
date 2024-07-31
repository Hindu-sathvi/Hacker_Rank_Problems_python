#https://www.hackerrank.com/challenges/text-wrap/problem?isFullScreen=true
#text-wrap
#code
import textwrap
def wrap(string, max_width):
    wrapped_lines = textwrap.wrap(string, max_width)
    return '\n'.join(wrapped_lines)
if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)
# Use textwrap.wrap to break the string into lines of max_width and Join the lines with newline characters and return
    