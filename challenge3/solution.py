# You have L, a list containing some digits (0 to 9). Write a function solution(L) which finds the largest number that can be made from some or all of these digits and is divisible by 3. If it is not possible to make such a number, return 0 as the solution. 
# L will contain anywhere from 1 to 9 digits. 
# The same digit may appear multiple times in the list, but each element in the list may only be used once.
# The solution should return an integer.
# The defect on this solution is that it doesn't check that the combination of two digits removed is the largest possible combination. 
# For example, if the list is [2, 3, 4, 5, 6, 7, 8, 9], the solution will be 9765432 instead of 9876543.

#

def solution(l):

    if len(l) == 0:
        return 0

    # Check for numbers numbers in the list not between 0 and 9
    for i in l:
        if i < 0 or i > 9:
            return 0

    # Sort the list in descending order
    l.sort(reverse=True)
    
    max = sum(l)

    if max % 3 == 0:
        return int("".join(map(str, l)))
        
    # Check with one digit removed
    for i in range(len(l)):
        temp = l.copy()
        temp.pop(i)
        if sum(temp) % 3 == 0:
            return int(''.join(map(str, temp)))
        
    # Check with two digits removed
    for i in range(len(l)):
        for j in range(i+1, len(l)):
            temp = l.copy()
            temp.pop(j)
            temp.pop(i)
            if sum(temp) % 3 == 0:
                return int(''.join(map(str, temp)))
    return 0


# Write an assertion to test your solution.
assert solution([3, 1, 4, 1]) == 4311
assert solution([3, 1, 4, 1, 5, 9]) == 94311
assert solution([1, 1, 1, 1]) == 111
assert solution([2, 2, 2, 2]) == 222
assert solution([1,3,7]) == 3
assert solution([2,3,5]) == 3
assert solution([]) == 0
assert solution([3,2,9,4,0,-1]) == 0
print(solution([2, 3, 4, 5, 6, 7, 8, 9]))