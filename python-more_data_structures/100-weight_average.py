#!/usr/bin/python3
def weight_average(my_list=[]):
    """
    Returns the weighted average of all integers in a list of tuples.
    
    Args:
        my_list: A list of tuples in the format (<score>, <weight>).
        
    Returns:
        The weighted average, or 0 if the list is empty.
    """
    if not my_list:
        return 0

    total_weighted_score = 0
    total_weight = 0

    for score, weight in my_list:
        total_weighted_score += score * weight
        total_weight += weight

    return total_weighted_score / total_weight
