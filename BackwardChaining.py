from Production import AND, OR, NOT, IF, THEN, match, populate, simplify

def backchain_to_goal_tree(rules, hypothesis):
    subgoals = [hypothesis]
    for rule in rules:
        consequent = rule.consequent()
        bindings = match(consequent, hypothesis)
        if bindings is not None:
            antecedent = rule.antecedent()
            populated_antecedent = populate(antecedent, bindings)
            subgoals.append(backchain_to_goal_tree(rules, populated_antecedent))
    
    return simplify(OR(*subgoals))

# Example usage with zookeeper rules
from data import zookeeper_rules

if __name__ == "__main__":
    hypothesis = 'opus is a penguin'
    goal_tree = backchain_to_goal_tree(zookeeper_rules, hypothesis)
    print("Goal Tree for the Hypothesis '{}':".format(hypothesis))
    print(goal_tree)
