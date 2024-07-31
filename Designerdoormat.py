#https://www.hackerrank.com/challenges/designer-door-mat/problem?isFullScreen=true
#designer-door-mat
#code
def generate_door_mat(N, M):
    pattern = []

    # Top half of the pattern
    for i in range(1, N, 2):
        line = ('.|.' * i).center(M, '-')
        pattern.append(line)

    # Middle line with 'WELCOME'
    welcome_line = 'WELCOME'.center(M, '-')
    pattern.append(welcome_line)

    # Bottom half of the pattern (mirror of the top half)
    for i in range(N-2, 0, -2):
        line = ('.|.' * i).center(M, '-')
        pattern.append(line)

    return "\n".join(pattern)

if __name__ == '__main__':
    N, M = map(int, input().split())
    result = generate_door_mat(N, M)
    print(result)