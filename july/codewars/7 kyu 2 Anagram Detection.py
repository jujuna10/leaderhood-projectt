def is_anagram(test, original):
    test_d = test.lower()
    original_d = original.lower()
    for i in test:
        a = sorted(test_d)
    for j in original:
        b = sorted(original_d)
    if a == b:
        return True
    else:
        return False