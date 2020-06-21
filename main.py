def is_even(n):
    return True # FIXME

def even_numbers_using_an_array():
    result = []
    for n in range(1, 10):
        if is_even(n):
            result.append(n)
    return result


def even_numbers_using_yield():
    for n in range(1, 10):
        if is_even(n):
            yield n


# Main code
for even_number in even_numbers_using_an_array():
    print(even_number)

for even_number in even_numbers_using_yield():
    print(even_number)
