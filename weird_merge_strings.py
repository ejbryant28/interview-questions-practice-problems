# You are implementing your own programming language and you've decided to add support for merging strings. A typical merge function would take two strings s1 and s2, and return the lexicographically smallest result that can be obtained by placing the symbols of s2 between the symbols of s1 in such a way that maintains the relative order of the characters in each string.

# For example, if s1 = "super" and s2 = "tower", the result should be merge(s1, s2) = "stouperwer".

def assign_values(string):

    character_count = {}

    for char in string:
        if char in character_count:
            character_count[char] += 1

        else:
            character_count[char] = 1

    return character_count

def mergeStrings(s1, s2):

    merged = ''

    s1_counts = assign_values(s1)
    s2_counts = assign_values(s2)

    while s1 or s2:

        #if either string is empty, add the other completely to merged and set string to be empty
        if not s1:
            merged = merged + s2
            s2 = ''
        elif not s2:
            merged = merged + s1
            s1 = ''

        #if the counts are equal the lower one comes first
        elif s1_counts[s1[0]] == s2_counts[s2[0]]:
            if s1[0] <= s2[0]:
                merged = merged + s1[0] + s2[0]
            else:
                merged = merged + s2[0] + s1[0]

            s1 = s1[1:]
            s2 = s2[1:]

        elif s1_counts[s1[0]] < s2_counts[s2[0]]:
            merged = merged + s1[0]
            s1 = s1[1:]
        else:
            merged = merged + s2[0]
            s2 = s2[1:]

    return merged

print(mergeStrings('super', 'tower'))
print(mergeStrings('dce', 'cccbd'))


# print(assign_values('super'))
# print(assign_values('tower'))
