class Rule:
    def __init__(self, conditions, conclusion):
        self.conditions = set(conditions)
        self.conclusion = conclusion


class ExpertSystem:
    def __init__(self):
        self.facts = set()
        self.rules = []
        self.inference_log = []

    def add_fact(self, fact):
        self.facts.add(fact)

    def add_rule(self, rule):
        self.rules.append(rule)

    def forward_chaining(self):
        new_inferred = True

        while new_inferred:
            new_inferred = False

            for rule in self.rules:
                if rule.conditions.issubset(self.facts) and rule.conclusion not in self.facts:
                    
                    self.facts.add(rule.conclusion)
                    new_inferred = True
                    
                    log_message = f"Applied Rule: IF {rule.conditions} THEN {rule.conclusion}"
                    self.inference_log.append(log_message)

    def show_results(self):
        print("\nFinal Facts:")
        for fact in self.facts:
            print("-", fact)

        print("\nInference Steps:")
        for step in self.inference_log:
            print(step)


# -------------------------------
# Create Expert System
# -------------------------------
system = ExpertSystem()

# Define rules
system.add_rule(Rule(["fever", "cough"], "flu"))
system.add_rule(Rule(["flu", "body_ache"], "severe_flu"))
system.add_rule(Rule(["fever", "rash"], "measles"))

# Take user input
user_input = input("Enter symptoms separated by comma: ")
symptoms = [s.strip() for s in user_input.split(",")]

for symptom in symptoms:
    system.add_fact(symptom)

# Run forward chaining
system.forward_chaining()

# Show results
system.show_results()