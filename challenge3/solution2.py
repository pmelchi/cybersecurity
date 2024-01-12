# You have L, a list containing some digits (0 to 9). Write a function solution(L) which finds the largest number that can be made from some or all of these digits and is divisible by 3. If it is not possible to make such a number, return 0 as the solution. 
# L will contain anywhere from 1 to 9 digits. 
# The same digit may appear multiple times in the list, but each element in the list may only be used once.
# The solution should return an integer.
#

def solution(l):
    # sort in decending order
    l = sorted(l, reverse = True)
    # if the number is already divisible by three
    if sum(l) % 3 == 0:
        # return the number
        return int("".join(str(n) for n in l))
    possibilities = [0]
    # try every combination of removing a single digit
    for i in range(len(l)):
        # copy list of digits
        _temp = l[:]
        # remove a digit
        del _temp[len(_temp) - i - 1]
        # check if it is divisible by three
        if sum(_temp) % 3 == 0:
            # if so, this is our solution (the digits are removed in order)
            return int("".join(str(n) for n in _temp))
        # try every combination of removing a second digit
        for j in range(1, len(_temp)):
            # copy list of digits again
            _temp2 = _temp[:]
            # remove another digit
            del _temp2[len(_temp2) - j - 1]
            # check if this combination is divisible by three
            if sum(_temp2) % 3 == 0:
                # if so, append it to the list of possibilities
                possibilities.append(int("".join(str(n) for n in _temp2)))
    # return the largest solution
    return max(possibilities)

assert solution([3, 1, 4, 1]) == 4311
assert solution([3, 1, 4, 1, 5, 9]) == 94311
assert solution([1, 1, 1, 1]) == 111
assert solution([2, 2, 2, 2]) == 222
assert solution([1,3,7]) == 3
assert solution([2,3,5]) == 3
# assert solution([]) == 0
#print(solution([0, -1, -2, 3, 4, 5, 6, 7, 8, 9]))
print(solution([2, 3, 4, 5, 6, 7, 8, 9]))
# print(solution([1, 0, 0, 0, 0 ]))
# print(solution([3, 0, 0, 0, 0 ]))
# print(solution(['A', 'B']))
# print(solution([7, 4, 3]))
# print(solution([7, 7, 4]))
# print(solution([1,3,7, 0]))
# print(solution([3]))
# print(solution([2, 1]))
# print("All test cases passed!")