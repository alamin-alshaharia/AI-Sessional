# Define Modus Tollens function for FOL
def modus_tollens(p_implies_q, not_q):
    return p_implies_q and not_q

# Define facts
symptoms = {}
diseases = {'Bob': []}  # Bob has no disease
# Define predicates
def HasSymptom(person, symptom):
    return symptoms.get((person, symptom), False)
def HasDisease(person, disease):
    return disease in diseases.get(person, [])

# Rule: If a person has DiseaseA, they will have SymptomA
def disease_rule(person):
    if HasDisease(person, 'DiseaseA'):
        symptoms[(person, 'SymptomA')] = True

# Given: Bob does not have SymptomA
not_symptom_a = not HasSymptom('Bob', 'SymptomA')

# Apply Modus Tollens: If "DiseaseA -> SymptomA" and "¬SymptomA", then "¬DiseaseA"
if modus_tollens(True, not_symptom_a):
    diseases['Bob'] = []  # Confirm Bob does not have DiseaseA

# Check if Bob has DiseaseA
has_disease_a = HasDisease('Bob', 'DiseaseA')
print("Does Bob have DiseaseA?", has_disease_a)
