###### some bad code we see #########

s = [88, 92, 79, 93, 85]
print(sum(s) / len(s))

s1 = []
for x in s:
    s1.append(x + 5)

print(sum(s1) / len(s1))


s2 = []
for x in s:
    s2.append(x + 10)

print(sum(s2) / len(s2))


s3 = []
for x in s:
    s3.append(x ** 0.5 * 10)

print(sum(s3) / len(s3))


####### little better #########

import math
import numpy as np

test_scores = [88, 92, 79, 93, 85]
print(np.mean(test_scores))

curved_5 = [score + 5 for score in test_scores]
print(np.mean(curved_5))

curved_10 = [score + 10 for score in test_scores]
print(np.mean(curved_10))


curved_sqrt = [math.sqrt(score) * 10 for score in test_scores]
print(np.mean(curved_sqrt))


######## codes with function with two purposes, consider refactoring #####

import math
import numpy as np


def flat_curve(arr, n):
    curved_arr = [i + n for i in arr]
    print(np.mean(curved_arr))
    return curved_arr


def square_root_curve(arr):
    curved_arr = [math.sqrt(i) * 10 for i in arr]
    print(np.mean(curved_arr))
    return curved_arr


test_scores = [88, 92, 79, 93, 85]
curved_5 = flat_curve(test_scores, 5)
curved_10 = flat_curve(test_scores, 10)
curved_sqrt = square_root_curve(test_scores)


########### with some abstraction on the ligic #############


import math
import numpy as np


def flat_curve(arr, n):
    return [i + n for i in arr]


def square_root_curve(arr):
    return [math.sqrt(i) * 10 for i in arr]


test_scores = [88, 92, 79, 93, 85]
curved_5 = flat_curve(test_scores, 5)
curved_10 = flat_curve(test_scores, 10)
curved_sqrt = square_root_curve(test_scores)


for score_list in test_scores, curved_5, curved_10, curved_sqrt:
    print(np.mean(score_list))


############ Example 1 ################

def numeric_to_buckets(df, column_name):
    median = df[column_name].median()
    for i, val in enumerate(df[column_name]):
        if val >= median:
            df.loc[i, column_name] = 'high'
        else:
            df.loc[i, column_name] = 'low'


for feature in df.columns[:-1]:
    numeric_to_buckets(df, feature)
    print(df.groupby(feature).quality.mean(), '\n')

############# Example 2 ####################

start = time.time()

total_price = 0
for cost in gift_costs:
    if cost < 25:
        total_price += cost * 1.08  # add cost after tax

print(total_price)
print('Duration: {} seconds'.format(time.time() - start))


#############################################

start = time.time()

total_price = np.sum(cost * 1.08 for cost in gift_costs if cost < 25)
print(total_price)

print('Duration: {} seconds'.format(time.time() - start))

#################################################

start = time.time()

total_price = (gift_costs[gift_costs < 25]).sum() * 1.08
print(total_price)

print('Duration: {} seconds'.format(time.time() - start))

