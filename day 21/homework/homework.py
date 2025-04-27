#codewars
def check_alive(health):
    return health > 0

def cookie(x):
    if isinstance(x, str):
        name = "Zach"
    elif isinstance(x, (int, float)) and not isinstance(x, bool):
        name = "Monica"
    else:
        name = "the dog"
    return f"Who ate the last cookie? It was {name}!"


def century(year):
    return (year + 99) // 100



def find_average(numbers):
    return sum(numbers) / len(numbers)
