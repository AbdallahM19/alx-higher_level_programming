#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0
    total_score = 0
    total_weight = 0
    total = 0
    for i, x in my_list:
        total_score += i * x
        total_weight += x
    if total_weight == 0:
        return 0
    total = total_score / total_weight
    return total
