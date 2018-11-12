
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

def longestCommonPrefix(strs):
    """
    :type strs: List[str]
    :rtype: str
    """

    if not strs:
        return ''

    prefix = []

    for char in zip(*strs):
        char_set = set(char)

        if len(char_set) != 1:
            break

        prefix += char_set.pop()

    return ''.join(prefix)


assert(longestCommonPrefix(["flower","flow","alight"])== '')
assert(longestCommonPrefix(["flower","flow","flight"])== 'fl')
assert(longestCommonPrefix(["flower","flow","flowers"])== 'flow')

def strStr(haystack, needle):
    """
    :type haystack: str
    :type needle: str
    :rtype: int
    """
    
    if not needle:
        return 0
    
    for i in range(len(haystack) - len(needle) + 1):
        
        if haystack[i:i+len(needle)] == needle:
            return i
        
    return -1


assert(strStr('hello', 'll') == 2)
assert(strStr('dklsa;', 'sdfkls') == -1)
assert(strStr('skjdfl;', '') == 0)
assert(strStr('a', 'a') == 0)

def lengthOfLastWord(s):
    """
    :type s: str
    :rtype: int
    """
    
    sentence = s.split()
    
    if len(sentence) < 1:
        return 0
    
    return len(sentence[-1])

assert(lengthOfLastWord('a ')==1)
assert(lengthOfLastWord('')==0)
assert(lengthOfLastWord('hello world') == 5)


def plusOne(digits):
    """
    :type digits: List[int]
    :rtype: List[int]
    """
    
    num = 0
    r = 1
    
    for n in range(1, len(digits)+1):
        num += digits[-n] * r
        r *= 10
        
    num += 1
    new_digits = []
    
    j = 10
    while num:
        
        remainder = num % j
        dig = remainder * 10 // j
        
        new_digits.insert(0, dig)
        num -= remainder
        j *= 10
        
    return new_digits

assert(plusOne([1, 1, 1]) == [1, 1, 2])
assert(plusOne([1, 1, 9]) == [1, 2, 0])
assert(plusOne([9, 9]) == [1, 0, 0])


def romanToInt(s):
    """
    :type s: str
    :rtype: int
    """
    
    roman_to_int = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
    
    ints = []
    
    for roman in s:
        ints.append(roman_to_int[roman])

    check = list(sorted(ints))
    check = list(reversed(check))
    # print(check.reverse)
        
    if check == ints:
        return sum(ints)
    
    num = 0
    
    #[1000, 100, 1000, 10, 100, 1, 5]
    #[[1000], [100, 1000], [10, 100], [1, 5]]
    #[1000, 900, 90, 4]

    #[10, 100, 5, 1]
    #[[10, 100], [5] [1]]
    
    grouped = []
    
    while ints:

        if len(ints) == 1:
            n = ints.pop()
            grouped.append([n])

        elif ints[-1] <= ints[-2]:
            n = ints.pop()
            grouped.append([n])

        else:
            group = ints[-2:]
            grouped.append(group)
            ints[-2:] = []

    for i, group in enumerate(grouped):

        if len(group) == 1:
            grouped[i] = group[0]

        else:
            num = group[1] - group[0]
            grouped[i] = num




    return sum(grouped)
    
assert(romanToInt('III') == 3)
assert(romanToInt('IV') == 4)
assert(romanToInt('MCMXCIV') == 1994)
assert(romanToInt('XIII') == 13)
assert(romanToInt('XLVIII') == 48)

def searchInsert(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: int
    """
    
    #[1, 2, 3, 4], 5 --> 4
    #[1, 2, 3, 4], 4 --> 3
    #[1, 4, 5, 6], 3 --> 1
    #[], 2 --> 0
    
    if not nums or target <= nums[0]:
        return 0
    
    if target > nums[-1]:
        return len(nums)
    
    if target == nums[-1]:
        return len(nums) - 1
    
    for i, num in enumerate(nums):
        
        if num == target:
            return i
        
        elif num > target:
            return i

assert(searchInsert([1, 3, 5, 6], 2) == 1)


def isPalindrome(s):
    """
    :type s: str
    :rtype: bool
    """
    
    #'A man, a plan, a canal: Panama' --> True
    #'amanaplanacanalpanama' == reverse?
    
    joined = []
    
    for letter in s:
        if letter.isalpha():
            joined.append(letter.lower())
    
    if joined == list(reversed(joined)):
        return True
    
    return False

# print(isPalindrome('OP'))
# print(isPalindrome(''))
# print('passed!')

def rev_int(n):

    #n, and new_num
    #n % 10, add the remainder times the total magnitude to new_num
    #multiply the 10 by 10, divide total magnitude by 10
    if n < 0:
        neg = True
        n = abs(n)

    else:
        neg = False

    rev = 0
    while n > 0:
        pop = n % 10
        n -= pop
        n /= 10

        rev = rev * 10 + pop

    if neg:
        return int(rev) * -1

    return int(rev)


assert(rev_int(123)== 321)
assert(rev_int(1)==1)
assert(rev_int(-123)==-321)
assert(rev_int(0)==0)
assert(rev_int(12340)==4321)
assert(rev_int(1234)==4321)

def rev_int_2(n):

    if n < 0:
        neg = True
        n = abs(n)

    else:
        neg = False

    rev = 0

    while n > 0:
        pop = n % 10
        n -= pop
        n /= 10

        rev = rev * 10 + pop

    if neg:
        rev *= -1

    return rev

assert(rev_int_2(1234) == 4321)
assert(rev_int_2(190) == 91)
assert(rev_int_2(-1290) == -921)

print('passed!')

# print(rev_int(123))




