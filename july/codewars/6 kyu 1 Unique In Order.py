def unique_in_order(sequence):
    result = []
    for i in sequence:
        if len(result) < 1 or not i == result[len(result) -1]:
            result.append(i)
    return result