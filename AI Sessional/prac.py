# Define the facts using a dictionary to represent parent relationships
parents = {
    ('John', 'Mary'): True,
    ('Mary', 'Joe'): True
}

# Define the Parent predicate function
def Parent(x, y):
    """Returns True if x is the parent of y, based on defined facts."""
    return parents.get((x, y), False)

# Define the Grandparent predicate function
def Grandparent(x, z):
    """
    Returns True if x is the grandparent of z, which means
    there exists a y such that Parent(x, y) and Parent(y, z).
    """
    # We need to find an intermediary person y such that:
    # Parent(x, y) and Parent(y, z)
    for y in ['Mary', 'Joe', 'John']:  # List of possible intermediary people
        if Parent(x, y) and Parent(y, z):
            return True
    return False

# Check if John is the grandparent of Joe
is_grandparent = Grandparent('John', 'Joe')
print("Is John the grandparent of Joe?", is_grandparent)
