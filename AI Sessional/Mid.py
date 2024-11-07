from itertools import product

# Define the truth values for propositions
truth_values = list(product([True, False], repeat=2))  # for 2 propositions (p, q)

# Function to print the truth table
def print_truth_table(statement_func, statement_name, variables=['p', 'q']):
    print(f"\nTruth Table for: {statement_name}")
    print(" | ".join(variables) + " | Result")
    print("-" * (len(variables) * 4 + 10))
    for values in product([True, False], repeat=len(variables)):
        result = statement_func(*values)
        print(" | ".join(str(v) for v in values) + f" | {result}")

# a. It is raining outside if and only if it is a cloudy day (p <-> q)
def statement_a(p, q):
    return p == q  # biconditional

# b. If you get a 100 on the final exam, then you earn an A in the class (p -> q)
def statement_b(p, q):
    return not p or q  # implication

# c. Take either 2 Advil or 3 Tylenol (p or q)
def statement_c(p, q):
    return p or q

# d. She studied hard or she is extremely bright (p or q)
def statement_d(p, q):
    return p or q

# e. I am a rock and I am an island (p and q)
def statement_e(p, q):
    return p and q

# Print truth tables for each statement
print_truth_table(statement_a, "It is raining outside if and only if it is a cloudy day")
print_truth_table(statement_b, "If you get a 100 on the final exam, then you earn an A in the class")
print_truth_table(statement_c, "Take either 2 Advil or 3 Tylenol")
print_truth_table(statement_d, "She studied hard or she is extremely bright")
print_truth_table(statement_e, "I am a rock and I am an island")
