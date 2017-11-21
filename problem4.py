# Largest palindrome product
'''A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.'''

def palindrome(n):
    if str(n) == str(n) [::-1]:
        return True
    else:
        return False

def largest():
    num1 = 999
    result = []
    while num1 > 100:
        num2 = 990
        if num2 > num1:
            num2 = num1 - (num1 % 11)
        while num2 > 109:
            if palindrome(str(num1 * num2)):
                result.append(num1 * num2)
            num2 -= 11
        num1 -= 1
    result.sort()
    print (result[len(result) - 1])

largest()