# Given an integer n and an array a of length n, your task is to apply the following mutation to a:

#     Array a mutates into a new array b of length n.
#     For each i from 0 to n - 1, b[i] = a[i - 1] + a[i] + a[i + 1].
#     If some element in the sum a[i - 1] + a[i] + a[i + 1] does not exist, it should be set to 0. For example, b[0] should be equal to 0 + a[0] + a[1].

def mutateTheArray(n, a):

    #initialize b
    #iterate over a by index
        # if i is 0 or n-1, set first or last value to be 0
        # add the three values
        # append to b

    # return b

    b = []

    for i in range(n):

        if i == 0:
            first = 0
        else:
            first = a[i - 1]

        if i == n - 1:
            next_ = 0
        else:
            next_ = a[i + 1]

        b.append(first + a[i] + next_)

    return b

assert(mutateTheArray(5, [4, 0, 1, -2, 3]) == [4, 5, -1, 2, 1])
assert(mutateTheArray(1, [1]) == [1])
assert(mutateTheArray(0, []) == [])
