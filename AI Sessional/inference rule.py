# Rule of Inference Functions

def modus_ponens(p_implies_q, p):
    """Modus Ponens: If P → Q and P are true, then Q is true."""
    if p_implies_q and p:
        return True
    return False

def modus_tollens(p_implies_q, not_q):
    """Modus Tollens: If P → Q and ¬Q are true, then ¬P is true."""
    if p_implies_q and not_q:
        return True
    return False

def disjunctive_syllogism(p_or_q, not_p):
    """Disjunctive Syllogism: If P ∨ Q and ¬P are true, then Q is true."""
    if p_or_q and not_p:
        return True
    return False

def hypothetical_syllogism(p_implies_q, q_implies_r):
    """Hypothetical Syllogism: If P → Q and Q → R are true, then P → R is true."""
    if p_implies_q and q_implies_r:
        return True
    return False

def simplification(p_and_q):
    """Simplification: If P ∧ Q is true, then P is true (or Q is true)."""
    if p_and_q:
        return True
    return False

def conjunction(p, q):
    """Conjunction: If P and Q are true, then P ∧ Q is true."""
    if p and q:
        return True
    return False

def addition(p):
    """Addition: If P is true, then P ∨ Q is true for any Q."""
    if p:
        return True
    return False

# Example Usage
# Given: P -> Q is True, P is True
# Prove: Q is True
p_implies_q = True
p = True
q = modus_ponens(p_implies_q, p)
print("Result of Modus Ponens (If P → Q and P, then Q):", q)

# Given: P -> Q is True, ¬Q is True
# Prove: ¬P is True
not_q = True
not_p = modus_tollens(p_implies_q, not_q)
print("Result of Modus Tollens (If P → Q and ¬Q, then ¬P):", not_p)

# Given: P ∨ Q is True, ¬P is True
# Prove: Q is True
p_or_q = True
not_p = True
q = disjunctive_syllogism(p_or_q, not_p)
print("Result of Disjunctive Syllogism (If P ∨ Q and ¬P, then Q):", q)

# Given: P → Q is True, Q → R is True
# Prove: P → R is True
q_implies_r = True
p_implies_r = hypothetical_syllogism(p_implies_q, q_implies_r)
print("Result of Hypothetical Syllogism (If P → Q and Q → R, then P → R):", p_implies_r)

# Given: P ∧ Q is True
# Prove: P is True
p_and_q = True
p = simplification(p_and_q)
print("Result of Simplification (If P ∧ Q, then P):", p)

# Given: P is True, Q is True
# Prove: P ∧ Q is True
p = True
q = True
p_and_q = conjunction(p, q)
print("Result of Conjunction (If P and Q, then P ∧ Q):", p_and_q)

# Given: P is True
# Prove: P ∨ Q is True
p = True
p_or_q = addition(p)
print("Result of Addition (If P, then P ∨ Q):", p_or_q)
