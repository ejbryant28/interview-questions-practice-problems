
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

        while j>0:

            i = i*10 + j%10
            j = int(j/10)

        return True if i==x else False

assert(isPalindrome(123) == False)
assert(isPalindrome(0) == True)
assert(isPalindrome(-123456) == False)
assert(isPalindrome('') == None)

def removeDuplicates(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
        
    if not nums:
        return 0
    
    i = 0
    j = 1
    r = 1

    for j in range(len(nums)):

        if nums[i] != nums[j]:
            i+=1

        r += 1
            
    return i + 1

assert(removeDuplicates([1, 2, 2, 2, 2, 2, 3, 4])== 4)
assert(removeDuplicates([1, 2, 3, 3, 3, 3]) == 3)
assert(removeDuplicates([]) == 0)
assert(removeDuplicates([1, 1, 1, 1]) == 1)

def removeElement(nums, val):
    """
    :type nums: List[int]
    :type val: int
    :rtype: int
    """
    
    i = 0
    while i <= len(nums)-1:

        if nums[i] == val:
            del nums[i]

        else:
            i+=1

    return nums

assert(removeElement([0, 1, 2, 2, 3, 0, 4, 2], 2)== [0, 1, 3, 0, 4])
assert(removeElement([1, 1, 1, 1, 1], 2)== [1, 1, 1, 1, 1])
assert(removeElement([1, 1, 1, 1, 1], 1)== [])
assert(removeElement([], 4) == [])




def isValid(s):
    """
    :type s: str
    :rtype: bool
    """
    
    if not s:
        return False

    stack = []
    
    openers = set(['[', '{', '('])
    
    brackets = {']':'[', '}':'{', ')':'('}
    
    for char in s:
        if char in openers:
            stack.append(char)
            
        if char not in openers:
            if len(stack) == 0:
                return False
            
            elif brackets[char] == stack[-1]:
                stack.pop()
            
            else:
                return False
            
    if stack == []:
        return True
    
    return False

assert(isValid('{})') == False)
assert(isValid('') == False)
assert(isValid('{}[({})]') == True)

print('passed!')
