def find_pearson(series_1, series_2):
    """given 2 lists of ints, return the pearson correlation of those lists"""
    
    pair_list = []
    # sum_1 = 0
    # sum_2 = 0
    for i in range(len(series_1)):
        pair_list.append((series_1[i], series_2[i]))                 
                         
    #for some reason the sum function isn't working. I'm going to move on to the next test and hope I have time to debug this at the end
    sum_1 = sum(series_1)
    sum_2 = sum(series_2)

    squares_1 = sum([n * n for n in series_1])
    squares_2 = sum([n * n for n in series_2])

    product_sum = sum([n * m for n, m in pair_list])

    size = len(series_1)

    numerator = product_sum - ((sum_1 * sum_2) / size)

    denominator = sqrt(
        (squares_1 - (sum_1 * sum_1) / size) *
        (squares_2 - (sum_2 * sum_2) / size))

    return numerator / denominator