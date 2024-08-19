#https://www.hackerrank.com/challenges/polar-coordinates/problem?isFullScreen=true
import cmath
z = complex(input())
# Calculate modulus and phase
r = abs(z)
theta = cmath.phase(z)
# Print the results
print(f"{r:.3f}")
print(f"{theta:.3f}")

