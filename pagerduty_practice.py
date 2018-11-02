
def reverse(x):
    """
    :type x: int
    :rtype: int
    """
    import re
    num = str(x)
    pattern = r'\d'
    
    num_matches = re.findall(pattern, num)
    if num_matches[-1] == '0':
        num_matches = num_matches[:-1]

    if not num_matches:
        return 0
                             
    if num[0] == '-':
        num_matches.append('-')
    new_num = ''.join(reversed(num_matches))
                             
    return int(new_num)


def isPalindrome(x):
    """
    :type x: int
    :rtype: bool
    """
    num = [d for d in str(x)]

    if len(num) == 1:
        return True

    if not num:
        return

    rev = list(reversed(num))
    if num == rev:
        return True
    
    return False

assert(isPalindrome(123) == False)
assert(isPalindrome(0) == True)
assert(isPalindrome(-123456) == False)
assert(isPalindrome('') == None)


def is_palidrome_2(x):
        
        if not x:
            return
        
        if x<0: 
            return False

        i,j = 0,x

        r = 0

        while j>0:

            i = i*10 + j%10
            j = int(j/10)
            r=+1

        return True if i==x else False

assert(isPalindrome(123) == False)
assert(isPalindrome(0) == True)
assert(isPalindrome(-123456) == False)
assert(isPalindrome('') == None)

print('passed!')
