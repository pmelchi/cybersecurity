def solution(i):
    if i < 0:
        return i

    return getPrimeString(i+5)
    

def next_prime(n):
    while True:
        n += 1
        for i in range(2, n):
            if n % i == 0:
                break
        else:
            return n

# Create a function that concatenates prime numbers up to a given string length 
def getPrimeString(length): 
    primeString = ""
    prime = 2
    while len(primeString) < length:
        primeString += str(prime)
        prime = next_prime(prime)
    return primeString[length -5:length]

print(solution(-1))
print(solution(0))
print(solution(3))
print(solution(20))
print(solution(41))