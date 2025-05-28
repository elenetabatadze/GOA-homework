def count_positives_sum_negatives(arr):
    
    if not arr:
        return []

  
    count_positives = 0
    sum_negatives = 0

    for num in arr:
        if num > 0:
            count_positives += 1  
        elif num < 0:
            sum_negatives += num 
       
    return [count_positives, sum_negatives]

def is_vow(arr):
   
    vowel_codes = {97, 101, 105, 111, 117}

    
    return [chr(num) if num in vowel_codes else num for num in arr]


def monkey_count(n):
    return list(range(1, n + 1))