import random


def generate_random_numbers():
    """
    Generate a list of random numbers
    """
    numbers = []
    for i in range(1000):
        numbers.append(random.randint(1, 100))
    return numbers


def find_duplicates():
    """
    Find duplicates in a list of random numbers
    """
    numbers = generate_random_numbers()
    duplicates = []
    for i in range(len(numbers)):
        for j in range(i+1, len(numbers)):
            if numbers[i] == numbers[j]:
                duplicates.append(numbers[i])
    return duplicates


print(find_duplicates())
