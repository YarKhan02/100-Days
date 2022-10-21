def palindrome(x):
    x = str(x)
    length = len(x)

    if length < 2:
        return 1
    
    if x[0] == x[length - 1]:
        return palindrome(x[1: length - 1])
        
    return 0

def sum_palindrome():
    n = str(input("Enter number: "))

    length = len(n)
    sum = 0

    for i in range(int(length)):
        x = int(n[i])
        sum += x

    result = palindrome(sum)

    return result

print(sum_palindrome())