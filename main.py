# Enter your code here. Read input from STDIN. Print output to STDOUT
import re

n = int(input())

for i in range(n):
    if bool(re.match(r'^[789][0-9]{9}(?![0-9])',input())):
        print("YES")
    else:
        print("NO")

