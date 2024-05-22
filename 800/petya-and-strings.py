import string

alphabet_dict = {letter: index for index, letter in enumerate(string.ascii_lowercase)}

def solve():
    first_string = input()
    second_string = input()
    flag = 0
    for i, _ in enumerate(first_string):
        if alphabet_dict[first_string[i].lower()] > alphabet_dict[second_string[i].lower()]:
            flag = 1
            break
        elif alphabet_dict[first_string[i].lower()] < alphabet_dict[second_string[i].lower()]:
            flag = -1
            break
    print(flag)
    
solve()