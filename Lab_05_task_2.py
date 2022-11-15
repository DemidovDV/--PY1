from random import randint, shuffle

def get_unique_list_numbers(n=15, begin=-10, end=11):
    numbers = [*range(begin, end)]
    while len(numbers) != n:
        numbers.pop(randint(0, len(numbers) - 1))
    shuffle(numbers)
    return numbers


list_unique_numbers = get_unique_list_numbers()
print(list_unique_numbers)
print(len(list_unique_numbers) == len(set(list_unique_numbers)))
