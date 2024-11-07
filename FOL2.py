parents = {
    ('John', 'Alice'): True,
    ('John', 'Bob'): True,
    ('Mary', 'Carol'): True,
    ('Mary', 'Dave'): True
}
# Define Parent predicate
def Parent(x, y):
    return parents.get((x, y), False)
# Define Sibling predicate
def Sibling(x, y):
    for parent in ['John', 'Mary']:  # Possible parent list
        if Parent(parent, x) and Parent(parent, y) and x != y:
            return True
    return False
# Define Cousin predicate
def Cousin(x, y):
    # Find parents of x and y
    parents_x = [p for p in ['John', 'Mary'] if Parent(p, x)]
    parents_y = [p for p in ['John', 'Mary'] if Parent(p, y)]

    # Check if the parents of x and y are siblings
    for px in parents_x:
        for py in parents_y:
            if Sibling(px, py):
                return True
    return False
# Check if Alice and Carol are cousins
is_cousin = Cousin('Alice', 'Carol')
print("Are Alice and Carol cousins?", is_cousin)
