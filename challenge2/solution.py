# The other solution is to walk the array starting from both ends at the same time and add the number of opposite signs that have added up to the current position.
# I think this solution is more elegant and efficient, but I'm not sure if it's more readable.

def solution(s):
    sum = 0
    for i in range(len(s)):
        if s[i] == '>':
            sum += s[i:].count('<')
    return sum * 2


# Test cases

print(solution('>----<'))
print(solution('<<>><"'))
print(solution('--->-><-><-->-'))