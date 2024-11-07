# Define Modus Ponens function for FOL
def modus_ponens(p_implies_q, p):
    return p_implies_q and p

# Define facts
likes = {('Alice', 'Bob'): True}
friends = {}

# Define predicates
def Likes(x, y):
    return likes.get((x, y), False)

def Friends(x, y):
    return friends.get((x, y), False)

# Implication rule: "If Alice likes Bob, then they are friends."
def friendship_rule():
    if Likes('Alice', 'Bob'):
        friends[('Alice', 'Bob')] = True

# Apply Modus Ponens: If "Alice likes Bob" and the rule is true, deduce friendship
if modus_ponens(Likes('Alice', 'Bob'), True):
    friendship_rule()

# Check if Alice and Bob are friends
are_friends = Friends('Alice', 'Bob')
print("Are Alice and Bob friends?", are_friends)
