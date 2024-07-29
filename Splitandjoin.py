#https://www.hackerrank.com/challenges/python-string-split-and-join/problem?isFullScreen=true
#python-string-split-and-join
#code
def split_and_join(line):
    # write your code here
      words = line.split(" ")
      result = "-".join(words)
      return result

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)