# Define facts
facts = {
    ('Parent', 'John', 'Mary'): True,
    ('Ancestor', 'Mary', 'Joe'): True
}

# Define predicates
def Parent(x, y):
    return facts.get(('Parent', x, y), False)

def Ancestor(x, y):
    return facts.get(('Ancestor', x, y), False)

# Inference rule (Modus Ponens)
def modus_ponens(p_implies_q, p):
    return p_implies_q and p

# Define the rule: If Parent(x, y) and Ancestor(y, z), then Ancestor(x, z)
def ancestor_rule(x, y, z):
    if Parent(x, y) and Ancestor(y, z):
        facts[('Ancestor', x, z)] = True

# Applying Universal Instantiation and Modus Ponens to deduce Ancestor(John, Joe)
ancestor_rule('John', 'Mary', 'Joe')

# Check if we successfully derived Ancestor(John, Joe)
is_ancestor = Ancestor('John', 'Joe')
print("Is John an ancestor of Joe?", is_ancestor)
