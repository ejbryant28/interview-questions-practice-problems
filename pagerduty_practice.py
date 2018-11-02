
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

    rev = list(reversed(num))
    if num == rev:
        return True
    
    return False

print(isPalindrome(121))
