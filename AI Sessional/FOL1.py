# Define facts
managers = {
    ('Alice', 'Bob'): True,
    ('Bob', 'Carol'): True
}

# Define Manager predicate
def Manager(x, y):
    return managers.get((x, y), False)

# Define WorksUnder predicate (recursive to account for hierarchy)
def WorksUnder(x, y):
    # Base case: Direct management
    if Manager(y, x):
        return True
    # Recursive case: Check if there's an intermediary manager z
    for z in ['Alice', 'Bob', 'Carol']:
        if Manager(y, z) and WorksUnder(x, z):
            return True
    return False

# Check if Carol works under Alice
works_under = WorksUnder('Carol', 'Alice')
print("Does Carol work under Alice?", works_under)
