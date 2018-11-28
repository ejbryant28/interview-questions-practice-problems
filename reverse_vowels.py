def reverseVowels(s):
    """
    :type s: str
    :rtype: str
    """
    
    # all_letters = s.split('')
    all_letters = list(s)
    vowels = []
    vowel_set = set(['a', 'e', 'i', 'o', 'u'])
    print(vowel_set)
    
    for a in all_letters:
        if a in vowel_set:
            vowels.append(a)

    print(all_letters)
    print(vowels)
            
    
    while vowels:
        for i, letter in enumerate(all_letters):

            if letter in vowel_set:
                current = vowels.pop()
                all_letters[i] = current
                
    return ''.join(all_letters)

print(reverseVowels('hello'))