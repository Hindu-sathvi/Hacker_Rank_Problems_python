#https://www.hackerrank.com/challenges/python-mutations/problem?isFullScreen=true
#python-mutations
#code
def mutate_string(string, position, character):
    modified_string = string[:position] + character + string[position + 1:]
    return modified_string
  
if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)