#cat years,dog years
def human_years_cat_years_dog_years(human_years):
    cat_years = 0
    dog_years = 0
    if human_years == 1:
        cat_years = 15
        dog_years = 15
            
    elif human_years == 2:
        cat_years = 24
        dog_years = 24
    elif human_years > 2:
        cat_years = 24 + ((human_years - 2) * 4)
        dog_years = 24 + ((human_years - 2) * 5)
    return [human_years,cat_years,dog_years]

#Sum of array singles
def repeats(arr):
    result = 0
    for i in arr:
        if arr.count(i) == 1:
            result += i
        else:
            pass
    return result

#Find the Mine!
def mine_location(field):
    result = []
    for i,l in enumerate(field):
        if 1 in l:
            result.append(i)
            result.append(field[i].index(1))
    return result

#Find Nearest square number
import math
def nearest_sq(n):
    sqrt_num = math.sqrt(n)
    near_num = round(sqrt_num)
    return near_num ** 2

#The Hashtag Generator
def generate_hashtag(s):
    
    
    result = "#"
    str = s.split()
    
    new_list = []
    for i in str:
        lower_word = i.lower()
        new_list += lower_word.title()
        
    
    for i in new_list:
        result += i.strip()
    if s == "" or len(result) > 140:
        return False
    return result

#Triangular Treasure
def triangular(n):
    if n <= 0:
        return 0
    elif n > 0:
        return n * (n + 1) // 2